## PDFsplitter

This Python script allows you to split a PDF file into separate PDF files, one for each page. It uses the PyPDF2 library to perform the splitting.

### Usage

1. Make sure you have Python 3.x installed on your system.

2. Install the required PyPDF2 library using pip:
```pip install PyPDF2```

3. Run the script with the following command:
    
    `python PDFsplitter.py input_pdf output_folder`
- `input_pdf`: The path to the input PDF file that you want to split.
- `output_folder`: The folder where the split PDF pages will be saved.

### Example

To split an input PDF file named `input.pdf` into separate pages and save them in an `output_pages` folder, you can run the following command:

    python PDFsplitter.py input.pdf output_pages