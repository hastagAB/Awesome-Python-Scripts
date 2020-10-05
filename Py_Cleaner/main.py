# Required Imports
import os
import shutil
import sys
from tkinter import *
import tkinter.messagebox as tmsg
from tkinter import filedialog

### File Extensions
exts = {
    'Images' : ['.jpeg', '.jpg', '.png', '.gif', '.bmp', '.ico', '.svg', '.tff'],
    'Medias' : ['.mp4', '.mp3', '.mkv', '.mov', '.3gp', '.wav', '.wmv', '.aac', '.flv', '.webm'],
    'Docs' : ['.pdf', '.docx', '.doc', '.pptx', '.pages', '.key', '.txt', '.rtf', '.csv', '.xlsx', '.odt', '.ppt'],
    'Codes' : ['.py', '.pyc', '.dart', '.c', '.cpp', '.js', '.html', '.css', '.java', '.go', '.r', '.sh'],
    'Archives' : ['.rar', '.zip', '.7z', '.alzip', '.iso', '.dmg'],
    'Executables' : ['.exe', '.bat', '.command', '.apk', '.app']
}

def create_folder(folder_name):
    ''' Create Folder if does not exists '''
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

def select_folder():
	''' File Dialog Folder Selection '''
	file_path = filedialog.askdirectory()
	path.set(file_path)

def clean_dir():
	''' Organize the directory '''
	try:
		entry_path = path.get() # This path is extracted from entry widget

		if (entry_path != ''):
			if (os.path.isdir(entry_path)):

				os.chdir(entry_path)
				cwd_files = [file.lower() for file in os.listdir(os.getcwd())] # Get the CWD files

				file_name =  os.path.basename(sys.argv[0])  # Extract name of the script

				if os.path.isfile(file_name): # Exclude the main script in the cleaning process if it exists in the CWD
					cwd_files.remove(file_name)

				count_files = len(next(os.walk(os.getcwd()))[2])
				# os.walk yields 3-tuple (dirpath, dirnames, filenames) (Its a Generator)

				for file in cwd_files:

					if os.path.isfile(file):
						ext = os.path.splitext(file) # Split the file into its name and extension

						if (ext[1] in exts.get('Images')):
						    create_folder('Images')
						    shutil.move(file, './Images/')

						elif (ext[1] in exts.get('Medias')):
							create_folder('Media')
							shutil.move(file, './Media/')

						elif (ext[1] in exts.get('Docs')):
							create_folder('Docs')
							shutil.move(file, './Docs/')

						elif (ext[1] in exts.get('Codes')):
						    create_folder('Codes')
						    shutil.move(file, './Codes/')

						elif (ext[1] in exts.get('Archives')):
						    create_folder('Archives')
						    shutil.move(file, './Archives/')

						elif (ext[1] in exts.get('Executables')):
						    create_folder('Exec')
						    shutil.move(file, './Exec/')

						else:
							create_folder('Others')
							shutil.move(file, './Others/')


				tmsg.showinfo("SUCCESS!", f"Your Directory Has Been Cleaned :)\n{count_files} file(s) Have Been Cleaned")

			else:
				tmsg.showerror("ERROR!", "Directory Not Found :(")
		else:
			tmsg.showerror("ERROR!", "Directory Not Found :(")

	except OSError:
		tmsg.showerror("Error!", "Directory Not Found :(")

root = Tk()
root.geometry('600x490')
root.minsize('600','490')
root.maxsize('600','490')
root.title("PY-CLEAN")

####### Background Image
bg_img = PhotoImage(file='bg.gif')
img_label = Label(root, image=bg_img)
img_label.place(relwidth=1, relheight=1)

####### Header

header_frm = Frame(root, background='#e8ca5f', relief=SUNKEN, bd=3)
header_frm.config(highlightthickness=0, highlightcolor='#c6d166', highlightbackground='#c6d166')
header_frm.pack(pady=7,fill=X)

header = Label(header_frm, text='PY-CLEAN', background='#e8ca5f', foreground='#FF1493', font="helvetica 19 bold", pady=3, padx=3)
header.pack(pady=4, fill=X)

###### Entry
path = StringVar()

side_label = Label(root, text='Enter Path To Clean ->', font="comicsansms 14 bold", padx=3, pady=4, background='#97b0cf', foreground='#bf391f', bd=3, relief=SUNKEN)
side_label.config(highlightthickness=2)
side_label.pack(anchor='w', padx=14, pady=45)

entry = Entry(root, textvariable=path, width=26, font="comicsansms 19 bold", background='#97b0cf', foreground='#343638', relief=SUNKEN, bd=2.5)
entry.config(highlightthickness=2.5, highlightcolor='#97b0cf', highlightbackground='#97b0cf')
entry.place(relx=0.35, rely=0.217)


### Selection Dialog Box, Clear Buttons

select_label = Label(root, text='Select Folder From Here ->', font="comicsansms 14 bold", padx=3, pady=4, background='#97b0cf', foreground='#bf391f', bd=3, relief=SUNKEN)
select_label.config(highlightthickness=2)
select_label.pack(anchor='w', padx=14, pady=50)

img = PhotoImage(file='folder.png')

folder_btn_frame = Frame(root, relief=SOLID, bd=4, background='#2160ad')
folder_btn_frame.place(relx=0.45, rely=0.45)

folder_btn = Button(folder_btn_frame, image=img, cursor='hand', command=select_folder)
folder_btn.config(highlightthickness=2, highlightcolor='#2160ad', highlightbackground='#2160ad')
folder_btn.pack()

btn_frame = Frame(root, relief=SUNKEN, bd=4, background='#3e4957')
btn_frame.place(relx=0.22, rely=0.82)

clean_btn = Button(btn_frame, text='Clean Now', font='comicsansms 22 bold', foreground='seagreen', cursor='hand', command=clean_dir)
clean_btn.config(highlightthickness=2, highlightcolor='#c4d64f', highlightbackground='#c4d64f')
clean_btn.pack()

clear_btn_frame = Frame(root, relief=SUNKEN, bd=4, background='#3e4957')
clear_btn_frame.place(relx=0.55, rely=0.82)

clear_btn = Button(clear_btn_frame, text='Clear Path', font='comicsansms 22 bold', foreground='red', cursor='hand', command=lambda : path.set(''))
clear_btn.config(highlightthickness=2, highlightcolor='#c4d64f', highlightbackground='#c4d64f')
clear_btn.pack()


root.mainloop()
