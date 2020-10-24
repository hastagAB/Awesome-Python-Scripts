# Download Page as PDF:

Download a page as a PDF .

 #### Required Modules :
  - pyppdf
    ```bash
      pip3 install pyppdf
    ```
  - pyppyteer 
    ```bash
      pip3 install pyppeteer
    ```

 #### Examples of use :
 - Download a page:
 ```bash
    python download-page-as-pdf.py -l 'https://www.pudim.com'
 ```

 - Download a page and give a pdf name:
 ```bash
    python download-page-as-pdf.py -l 'https://www.pudim.com' -n 'pudim.pdf'
 ```
