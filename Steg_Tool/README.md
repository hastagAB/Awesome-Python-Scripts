# Steganography Tool

* Advanced Image Steganography Tool used to hide files inside Images.
* Uses LSB (Least Significant Bit) Algorithm to store file data inside the image
* Works with only .png format

Commands
```
python3 steg.py
```
Input
```
encode <input_image_name> <output_image_name> <file_name>

decode <encoded_image_name> <extracted_file_name>
```
Example
```
encode image.png image_new.png secret.txt
decode image_new.png secret_new.txt
```