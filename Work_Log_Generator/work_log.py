"""Get commits for the repo specified as parameter and write work log."""
import os
import sys
from pathlib import Path

import qdarkstyle
from github import Github
from github.GithubException import BadCredentialsException
from PyQt5 import Qt
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import QAction
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QComboBox
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QPlainTextEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QWidget

sys.settrace
APP_NAME = 'Work Log Generator'
RESOURCES_FOLDER = 'resources/'
ICON_PATH = RESOURCES_FOLDER + 'icone.ico'
LOADER_PATH = RESOURCES_FOLDER + 'loader.gif'
SAVE_ICON_PATH = RESOURCES_FOLDER + 'save.png'


class WorkLogPreviewer(QMainWindow):
    """
    Worklog previewer class.

    Extends QMainWindow
    """

    sig = pyqtSignal(str, name='update')

    def __init__(self, parent=None, repository=None, systemtray_icon=None):
        """Init window."""
        super(WorkLogPreviewer, self).__init__(parent)

        saveAct = QAction(QIcon(SAVE_ICON_PATH), '&Save', self)
        saveAct.setShortcut('Ctrl+S')
        saveAct.setStatusTip('Save work log')
        saveAct.triggered.connect(self.save)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(saveAct)

        self.repository = repository
        self.systemtray_icon = systemtray_icon

        self.statusBar()

        widget = QWidget()
        layout = QVBoxLayout()
        self.te = QPlainTextEdit()
        layout.addWidget(self.te)

        self.lbl = QLabel()
        self.lbl.hide()
        self.movie = QMovie(LOADER_PATH)
        self.lbl.setMovie(self.movie)
        hlayout = QHBoxLayout()
        hlayout.addStretch()
        hlayout.addWidget(self.lbl)
        hlayout.addStretch()
        layout.addLayout(hlayout)

        self.generate_log()

        widget.setLayout(layout)
        widget.setFixedSize(500, 500)
        self.setCentralWidget(widget)

        self.setWindowTitle(f'Work log for {repository.full_name}')
        self.setWindowIcon(QIcon(ICON_PATH))
        self.setLocale(QtCore.QLocale())
        self.adjustSize()

        self.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())

    def generate_log(self):
        """Launch thread used to generate log."""
        self.lbl.show()
        self.movie.start()
        self.sig.connect(self.display_log)
        self.workThread = WorkLogThread(self, self.repository, self.sig)
        self.workThread.start()

    def display_log(self, log):
        """Display log received from thread."""
        self.lbl.hide()
        self.movie.stop()
        self.te.setPlainText(log)
        btMessage = "Log generation successfull!"
        self.systemtray_icon.showMessage(
            APP_NAME, btMessage, QIcon(ICON_PATH), 5000)
        self.statusBar().showMessage(btMessage)

    def save(self):
        """Save log to file."""
        home = str(Path.home())
        self.output = ""
        self.output = QFileDialog.getSaveFileName(self,
                                                  'Save file',
                                                  home,
                                                  "ReST files (*.rst)")

        if self.output[0] is not "":
            with open(self.output[0], 'w') as f:
                f.write(self.te.toPlainText())

            btMessage = f'File saved as {self.output[0]}.'
        else:
            btMessage = "Can't save. No file specified."
        self.systemtray_icon.showMessage(
            APP_NAME, btMessage, QIcon(ICON_PATH), 5000)
        self.statusBar().showMessage(btMessage)


class MainWidget(QWidget):
    """
    Worklog Generator class.

    Extends QWidget
    """

    sig = pyqtSignal(list, name='update')

    def __init__(self, parent=None):
        """Init widget."""
        super(MainWidget, self).__init__(parent)

        layout = QVBoxLayout()

        self.parent = parent

        self.ght = QLineEdit()
        self.ght.setPlaceholderText("Github Token")
        self.ght_keyPressEvent = self.ght.keyPressEvent
        self.ght_original_style = self.ght.styleSheet()
        self.ght.keyPressEvent = self.line_keyPressEvent
        layout.addWidget(self.ght)

        self.btn = QPushButton("Connect to github")
        self.btn.clicked.connect(self.getRepos)
        layout.addWidget(self.btn)

        self.combo = QComboBox()
        self.combo.setDisabled(True)
        layout.addWidget(self.combo)

        self.btn_save = QPushButton("Open worklog")
        self.btn_save.setDisabled(True)
        self.btn_save.clicked.connect(self.open_log)
        layout.addWidget(self.btn_save)

        self.lbl = QLabel()
        self.lbl.hide()
        self.movie = QMovie(LOADER_PATH)
        self.lbl.setMovie(self.movie)
        hlayout = QHBoxLayout()
        hlayout.addStretch()
        hlayout.addWidget(self.lbl)
        hlayout.addStretch()
        layout.addLayout(hlayout)

        self.setLayout(layout)

        self.setLocale(QtCore.QLocale())

        self.sig.connect(self.add_repo_to_combobox)

    def line_keyPressEvent(self, event):
        """Detect enter or return key pressed."""
        if (event.key() == QtCore.Qt.Key_Enter
                or event.key() == QtCore.Qt.Key_Return):
            self.getRepos()
        else:
            self.ght_keyPressEvent(event)

    def open_log(self):
        """Build rst file from repository commits and opens it."""
        if self.parent is not None:
            self.parent.statusBar().showMessage('Opening preview.')

        repo = self.combo.itemData(self.combo.currentIndex())

        self.preview = WorkLogPreviewer(None,
                                        repo, self.parent.systemtray_icon)
        self.preview.show()

        if self.parent is not None:
            self.parent.statusBar().showMessage('Done.')

    def getRepos(self):
        """Get repos for user and add them in a combobox."""
        if self.ght.text() is not "":
            if self.parent is not None:
                self.parent.statusBar().showMessage('Fetching repos...')

            self.lbl.show()
            self.movie.start()
            self.ght.setStyleSheet(self.ght_original_style)
            token = self.ght.text()
            self.g = Github(token)

            try:
                if self.workThread is not None and self.workThread.isRunning():
                    return
            except AttributeError:
                pass
            finally:
                self.workThread = ConnectionThread(self, self.g, self.sig)
                self.workThread.start()

        else:
            self.ght.setStyleSheet("QLineEdit { border: 2px solid red; }")

    def add_repo_to_combobox(self, repo_list):
        """Add repos from repo_list to combobox."""
        if len(repo_list) is not 0:
            for repo in repo_list:
                self.combo.addItem(repo.full_name, repo)
            self.combo.setDisabled(False)
            self.btn_save.setDisabled(False)

        self.lbl.hide()
        self.movie.stop()


class WorkLogThread(QtCore.QThread):
    """Thread used to write work log from repository."""

    def __init__(self, parent, repository=None, sig=None):
        """Init thread."""
        super(WorkLogThread, self).__init__(parent)
        self.sig = sig
        self.repository = repository
        self.parent = parent

    def run(self):
        """Run thread."""
        message = "Journal de travail"
        restTructuredText = message + os.linesep
        restTructuredText += '=' * len(message) + os.linesep * 2
        for commit in self.repository.get_commits():
            com = commit.commit
            date = com.author.date
            restTructuredText += str(date) + os.linesep
            restTructuredText += '-' * len(str(date)) + os.linesep * 2
            restTructuredText += self.format_message_for_rst(com.message)
        self.sig.emit(restTructuredText)

    def format_message_for_rst(self, message):
        """Format message for a nice rst print."""
        new_message = ""
        split_message = message.splitlines()
        for i in range(len(split_message)):
            if i is not 0 and split_message[i] is not "":
                new_message += "- "
            new_message += split_message[i] + "\n" * 2
        return new_message


class ConnectionThread(QtCore.QThread):
    """Thread used to connect to github."""

    def __init__(self, parent, g=None, sig=None):
        """Init thread."""
        super(ConnectionThread, self).__init__(parent)
        self.g = g
        self.sig = sig
        self.parent = parent

    def run(self):
        """Run thread."""
        repo_list = []
        try:

            for repo in self.g.get_user().get_repos():
                repo_list.append(repo)

            if self.parent is not None:
                self.parent.parent.statusBar().showMessage('Done.')
                sys_tray = self.parent.parent.systemtray_icon
                sys_tray.showMessage(
                    APP_NAME, 'Connected to github', QIcon(ICON_PATH), 5000)
        except BadCredentialsException as e:
            if self.parent is not None:
                self.parent.parent.statusBar().showMessage(str(e))
        self.sig.emit(repo_list)


class Window(QMainWindow):
    """Personal mainWindow class."""

    def __init__(self, systemtray_icon=None, parent=None):
        """Init window."""
        super(Window, self).__init__(parent)

        self.systemtray_icon = systemtray_icon
        self.statusBar()
        self.widget = MainWidget(self)
        self.setCentralWidget(self.widget)

        self.resize(500, 200)
        self.setWindowTitle(APP_NAME)

        self.setWindowIcon(QIcon(ICON_PATH))

        self.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())

        helpAct = QAction('&Help', self)
        helpAct.setShortcut('Ctrl+H')
        helpAct.setStatusTip('Help')
        helpAct.triggered.connect(self.helper)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&About')
        fileMenu.addAction(helpAct)

    def helper(self):
        """Display help."""
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)

        msg.setText("This simple python script allows you to generate a "
                    "worklog in rst format based on your repo commits.")
        msg.setInformativeText("You need to generated a token first.")
        msg.setWindowTitle("Help")
        msg.setWindowIcon(QIcon(ICON_PATH))
        msg.setDetailedText("Simply generate a personnal access token and "
                            "enter it in the first field of the window."
                            "\r\n"
                            "In order to generate this token, go to "
                            "https://github.com/settings/tokens "
                            "under \"Personal access tokens\".")
        msg.exec_()


if __name__ == "__main__":
    app = QApplication(list(sys.argv))
    icon = QIcon(ICON_PATH)
    systemtray_icon = Qt.QSystemTrayIcon(icon, app)
    systemtray_icon.show()
    window = Window(systemtray_icon)
    window.show()
    sys.exit(app.exec_())
