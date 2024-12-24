# Image to Text Generator

A desktop application built with Python and Tkinter to extract text from images using the [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) engine. This tool allows users to load images, extract text, and save or copy the text efficiently.

## Features
- **Image Loading**: Supports multiple image formats like PNG, JPEG, BMP, and TIFF.
- **Text Extraction**: Extracts text from images using the Tesseract OCR engine.
- **Text Editing**: Displays extracted text in a text box for further editing.
- **Copy and Save**: Copy extracted text to the clipboard or save it as a text file.
- **Theme Options**: Multiple themes (light, dark, and color variations) for better user experience.
- **Character Count**: Displays the number of characters in the extracted text.

## Prerequisites
- Python 3.8 or later.
- Install the required dependencies using:
  ```bash
  pip install -r requirements.txt

## Tesseract OCR installed on your system.
On Windows, download from Tesseract's official site and configure its path in the script:
pytesseract.pytesseract.tesseract_cmd =_ r'C:\Program Files\Tesseract-OCR\tesseract.exe'_

# Output Screenshot
![image](https://github.com/user-attachments/assets/c0ef9bc7-cd31-4107-a761-7d866479e458)
