import locker

import os
import tkinter as tk
from tkinter import PhotoImage
from tkinter import messagebox
from tkinter import filedialog

cwd = os.getcwd()
if not os.path.exists('files/'):
	os.mkdir('files')

class Application(tk.Frame):
	def __init__(self, master):
		super().__init__(master=master)
		self.master = master
		self.pack()

		self.title_frame()
		self.main_frame()
		self.status_frame()

		self.folder_path = ''
		self.fname = ''

	def title_frame(self):
		self.title = tk.Label(self, bg='gray',font=("Helvetica", 14), anchor='w')
		self.title.configure(width=35, height=3)
		self.title['text'] = '\t Folder Locker / Unlocker'
		self.title.grid(row=0, column=0, columnspan=2)

	def body_frame(self):
		self.body = tk.Frame(self, width=390, height=230)
		self.body.grid(row=1, column=0, columnspan=2, pady=10)

	def status_frame(self):
		self.status = tk.Text(self, width=50, height=3, fg='dodger blue')
		self.status.insert(tk.END, 'The folder you lock will be hidden automatically\n')
		self.status.insert(tk.END, 'Use the app to unlock it back')
		self.status.configure(state='disabled')
		self.status.grid(row=2, column=0, columnspan=2)

	def main_frame(self):
		self.body_frame()

		self.lock_button = tk.Button(self.body, font =('Verdana', 15), command=self.lock_frame)
		self.lock_button['image'] = lock_icon
		self.lock_button['compound'] = tk.TOP
		self.lock_button['text'] = 'Lock \nFolder'
		self.lock_button.configure(width=120, height=120)
		self.lock_button.grid(row=0, column=0, padx=(0,30), pady=(20,7))

		self.unlock_button = tk.Button(self.body, font =('Verdana', 15), command=self.unlock_frame)
		self.unlock_button['image'] = unlock_icon
		self.unlock_button['compound'] = tk.TOP
		self.unlock_button['text'] = ' Unlock \nFolder'
		self.unlock_button.configure(width=120, height=120)
		self.unlock_button.grid(row=0, column=1, padx=(30,0), pady=(20,7))

	def lock_frame(self):
		self.body.destroy()
		self.body_frame()

		self.status.configure(state='normal')
		self.status.delete(1.0, tk.END)
		self.status.insert(tk.END, 'Choose a folder, enter password and click lock\n')
		self.status.insert(tk.END, 'folder to lock and hide the folder')
		self.status.configure(state='disabled')

		self.password = tk.StringVar()
		
		self.pathlabel = tk.Label(self.body, bg='white', fg='black',
							borderwidth=1, relief='groove', wraplength=150)
		self.pathlabel['text'] = 'Select Folder'
		self.pathlabel.configure(width=22, height=3)
		self.pathlabel.grid(row=0, column=0, pady=10, padx=15)

		self.choose_folder = tk.Button(self.body, image=choose_folder_icon)
		self.choose_folder['command'] = self.select_folder
		self.choose_folder.grid(row=0, column=1, padx=(20,5), pady=10)

		self.back = tk.Button(self.body, image=back_icon)
		self.back['command'] = self.go_back
		self.back.grid(row=0, column=2, padx=(20,5), pady=10)

		self.elabel = tk.Label(self.body, anchor='e')
		self.elabel['text'] = 'Enter Password'
		self.elabel.grid(row=1, column=0, pady=20)

		self.entry = tk.Entry(self.body)
		self.entry['textvariable'] = self.password
		self.entry.grid(row=1, column=1, columnspan=2, pady=20)

		self.lock =tk.Button(self.body, bg='green', width=20)
		self.lock['text'] = f'Lock Folder'
		self.lock['command'] = lambda : self.lock_folder(self.folder_path)
		self.lock.grid(row=2, column=0, columnspan=3)

	def unlock_frame(self):
		self.body.destroy()
		self.body_frame()

		self.password = tk.StringVar()

		self.pathlabel = tk.Label(self.body, bg='white', fg='black',
							borderwidth=1, relief='groove', wraplength=150)
		self.pathlabel['text'] = 'Select Folder'
		self.pathlabel.configure(width=22, height=3)
		self.pathlabel.grid(row=0, column=0, pady=2, padx=15)

		self.back = tk.Button(self.body, image=back_icon)
		self.back['command'] = self.go_back
		self.back.grid(row=0, column=1, padx=(20,5), pady=2)

		self.scrollbar = tk.Scrollbar(self.body, orient=tk.VERTICAL)
		self.scrollbar.grid(row=0,column=3, rowspan=4, sticky='ns')

		self.list = tk.Listbox(self.body, selectmode=tk.SINGLE,
					 yscrollcommand=self.scrollbar.set, selectbackground='sky blue')
		self.list.config(height=10)
		self.enumerate_folders()
		self.list.bind('<Double-1>', self.get_folder)

		self.scrollbar.config(command=self.list.yview)
		self.list.grid(row=0, column=2, rowspan=4)

		self.elabel = tk.Label(self.body, anchor='e')
		self.elabel['text'] = 'Enter Password'
		self.elabel.grid(row=1, column=0, columnspan=2, pady=(1,1))

		self.entry = tk.Entry(self.body)
		self.entry['textvariable'] = self.password
		self.entry.grid(row=2, column=0, columnspan=2)

		self.unlock =tk.Button(self.body, bg='green', width=20)
		self.unlock['text'] = f'Unlock Folder'
		self.unlock['command'] = lambda : self.unlock_folder(self.fname)
		self.unlock.grid(row=3, column=0, columnspan=2, pady=(10,0))

	def go_back(self):
		self.body.destroy()
		self.main_frame()

		self.status.configure(state='normal')
		self.status.delete(1.0, tk.END)
		self.status.insert(tk.END, 'The folder you lock will be hidden automatically\n')
		self.status.insert(tk.END, 'Use the app to unlock it back')
		self.status.configure(state='disabled')

	def select_folder(self):
		self.folder_path = filedialog.askdirectory(initialdir=cwd)
		self.pathlabel['anchor'] = 'w'
		self.pathlabel['text'] = self.folder_path

	def enumerate_folders(self):
		self.dct = locker.read_json()
		self.folders_list = list(self.dct.keys())

		self.status.configure(state='normal')
		self.status.delete(1.0, tk.END)

		if len(self.folders_list) > 0:
			for index, fname in enumerate(self.folders_list):
				self.list.insert(index, fname)
			self.status.insert(tk.END, 'Choose a folder, enter password and click unlock\n')
			self.status.insert(tk.END, 'folder to unlock the folder')
		else:
			self.status.insert(tk.END, '0 folders locked yet\n')
			
		self.status.configure(state='disabled')

	def get_folder(self, event):
		if event is not None:
			self.current = self.list.curselection()[0]
			self.folder_path = self.dct[self.folders_list[self.current]][0]
			self.key = self.dct[self.folders_list[self.current]][1]
			self.pathlabel['text'] = self.folder_path

	def lock_folder(self, path):
		password = self.entry.get()
		if not self.folder_path == '':
			if len(password) <= 4:
				messagebox.showerror('Failed to lock', 'password is too short')
			else:
				status = locker.lock(self.folder_path, password)
				if status == 'failed':
					messagebox.showerror('Failed to lock', 'A folder with this name already locked')
				else:
					messagebox.showinfo('Folder status', 'Locked successfully')
		self.password.set('')
		self.pathlabel['anchor'] = 'c'
		self.pathlabel['text'] = 'Select Folder'

	def unlock_folder(self, fname):
		password = self.entry.get()
		if not self.folder_path == '':
			if len(password) <= 4:
				messagebox.showerror('Failed to unlock', 'password is too short')
			else:
				status = locker.unlock(self.folder_path, password, self.key)
				if status == 'failed':
					messagebox.showerror('Failed to unlock', 'Incorrect Password')
				else:
					messagebox.showinfo('Folder status', 'Folder unlocked successfully')
		self.password.set('')
		self.pathlabel['anchor'] = 'c'
		self.pathlabel['text'] = 'Select Folder'
		self.list.delete(0, tk.END)
		self.enumerate_folders()

if __name__ == '__main__':
	root = tk.Tk()
	root.geometry('400x305')
	root.title('Folder Locker/Unlocker')
	root.resizable(0,0)

	lock_icon = PhotoImage(file='icons/lock.png').subsample(2,2)
	unlock_icon = PhotoImage(file='icons/unlock.png').subsample(2,2)
	back_icon = PhotoImage(file='icons/back.png')
	choose_folder_icon = PhotoImage(file='icons/choose_folder.png')

	app = Application(master=root)
	app.mainloop()