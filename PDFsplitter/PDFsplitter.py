import PyPDF2
import argparse
import os


def split_pdf(input_pdf_path, output_folder):
    # Open the PDF file
    pdf_file = open(input_pdf_path, "rb")
    input_pdf_name = os.path.basename(input_pdf_path).split(".")[0]
    pdf_reader = PyPDF2.PdfReader(pdf_file)

    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Loop through each page and save it as a separate PDF file
    for page_num in range(len(pdf_reader.pages)):
        pdf_writer = PyPDF2.PdfWriter()
        pdf_writer.add_page(pdf_reader.pages[page_num])

        output_pdf_path = os.path.join(
            output_folder, f"{input_pdf_name}_{page_num + 1}.pdf"
        )

        with open(output_pdf_path, "wb") as output_pdf:
            pdf_writer.write(output_pdf)
            print(f"Page {page_num + 1} saved as {output_pdf_path}")

    # Close the input PDF file
    pdf_file.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Split a PDF file into separate pages")
    parser.add_argument(
        "input_pdf", help="Input PDF file path")
    parser.add_argument(
        "output_folder", help="Output folder path for split pages")
    args = parser.parse_args()

    input_pdf_path = args.input_pdf
    output_folder = args.output_folder

    split_pdf(input_pdf_path, output_folder)
