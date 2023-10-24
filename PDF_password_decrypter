import os
import PyPDF2
from tkinter import *
from tkinter import filedialog

# Create a GUI window using tkinter
root = Tk()
root.configure(background='grey')
root.title('PDF Password Remover')
root.geometry('300x350')

# this is the method select_file which when invoked uses filedialog to open a file and store the path of the file in the variable file_path
def select_file():
    global file_path
    file_path = filedialog.askopenfilename()

    # Creating a label to show the file path
    Label(root, text=file_path, bg='grey', fg='white').pack(pady=10)

# this is the method decrypt which when invoked decrypts the file using the password provided by the user
def decrypt():
    passwd = password.get() # getting the password from the entry widget

    # Opening the PDF file with a password
    pdf_file = open(file_path, 'rb')
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    if pdf_reader.is_encrypted:
        pdf_reader.decrypt(passwd)

    # Create a new PDF file without password protection
    pdf_writer = PyPDF2.PdfWriter()
    length = len(pdf_reader.pages)
    for page_num in range(length):
        pdf_writer.add_page(pdf_reader.pages[length - page_num - 1])

    # Creating a new file with the name provided by the user
    new_file_name = new_file.get()+".pdf"
    new_pdf_file = open(new_file_name, 'wb')
    pdf_writer.write(new_pdf_file)

    # Closing the files
    pdf_file.close()
    new_pdf_file.close()

    # Showing the file in a tkinter window
    show_pdf()

# this is a method that has a canvas of 500x700 resizeable to show the pdf file
# def show_pdf():
#     pdf_file = open(new_file.get()+".pdf", 'rb')
#     pdf_reader = PyPDF2.PdfReader(pdf_file)
#     page = pdf_reader.pages[0] 
#     page_content = page.extract_text()
#     print(page_content)
#     pdf_file.close()

def show_pdf():
    pdf_file = new_file.get()+".pdf"
    os.system(f"evince {pdf_file}")


# Button to choose the file to be decrypted
Button(root, text='Select File', bg='white', font=('arial', 12, 'normal'), command=select_file).pack(pady=20)

# Label widget to show the password
Label(root, text='Password: ', bg='grey', fg = 'white', font=('arial', 12, 'normal')).pack()

# Entry widget to accept the password
password = Entry(root,text='Password', width=20, font=('arial', 12, 'normal'), show='*', border=2)
password.pack(pady=20)

# Label widget to show the name with which the new file would be stored
Label(root, text='New File Name:', bg='grey', fg = 'white', font=('arial', 12, 'normal')).pack()

# Entry widget to accept the name with which the new file would be stored
new_file = Entry(root,text='New File Name', width=20, font=('arial', 12, 'normal'), border=2)
new_file.pack(pady=20)

# Button to decrypt the file
Button(root, text='Decrypt', bg='white', font=('arial', 12, 'normal'), command=decrypt).pack(pady=20)

root.mainloop()
