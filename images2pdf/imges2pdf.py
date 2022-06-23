import PyPDF2
from os import path
import sys

def File_existance_checker(filePath):
    if path.isfile(filePath):
        return filePath
    else:
        print("[-] Provide a valid File")
        sys.exit(1)
pdf_stored_path=input("Enter the name of you pdf file (please use backslash when typing in directory path):")

textFile_stored_path=path.join(path.dirname(pdf_stored_path),path.basename(pdf_stored_path).replace(".pdf",".txt"))
pdf_stored_path=File_existance_checker(pdf_stored_path)

print(textFile_stored_path)

with open(pdf_stored_path,'rb') as pdf_object:
    pdf_read=PyPDF2.PdfFileReader(pdf_object)
    
    pdf_pages=pdf_read.numPages
    
    for i in range(pdf_pages):
        page_object=pdf_read.getPage(i)
        with open(textFile_stored_path,'a+') as f:
            f.write((page_object.extract_text()))
    print(f"[+] Pdf Text has been extracted and written to {path.basename(textFile_stored_path)}")
