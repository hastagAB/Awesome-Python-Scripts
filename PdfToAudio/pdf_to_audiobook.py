# Importing the required packages.
import PyPDF2
import pyttsx3

text = None

# Reading a PDF file from your computer by specifying the path and setting the read mode to binary.
pdf_reader = PyPDF2.PdfFileReader(open(r"D:\MyPdf.pdf", "rb"))

# Getting the handle to speaker i.e. creating a reference to pyttsx3.Engine instance.
speaker = pyttsx3.init()

# Splitting the PDF file into pages and reading one at a time.
for page_number in range(pdf_reader.numPages):
    text = pdf_reader.getPage(page_number).extractText()
    # Generating speech.
    speaker.say(text)
    speaker.runAndWait()

# Stopping the speaker after the complete audio has been created.
speaker.stop()

# Saving the audiobook to your computer.
engine = pyttsx3.init()
engine.save_to_file(text, r"D:\MyAudio.mp3")
engine.runAndWait()
