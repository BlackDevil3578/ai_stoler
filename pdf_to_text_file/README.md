# PDF-to-Text OCR with Image Preprocessing

This project extracts text from PDF files by converting each page into high-resolution images and applying Optical Character Recognition (OCR) using Tesseract. It also includes image preprocessing steps to enhance the quality of the OCR results.

You need this code if you have pdf files that you can't select or use their text (text inside images) .
This code takes a pdf file path , creates a text file and save the extracted text in it.

## Features
- **PDF to Images Conversion**: Convert each page of a PDF into high-resolution PNG images.
- **Image Preprocessing**: Enhance images for better OCR accuracy using contrast adjustment and noise reduction.
- **OCR with Tesseract**: Extract text from images using Tesseract OCR.
- **Text Saving**: Automatically save the extracted text from each page into a `.txt` file.

## Dependencies
First you need to download Tesseract OCR .

To run the project, you'll need the following libraries:
- `PyMuPDF (fitz)`: For converting PDF pages to images.
- `Pillow`: For image manipulation and preprocessing.
- `OpenCV`: For converting images between different formats.
- `pytesseract`: For performing OCR on the images.
- `NumPy`: For handling image data arrays.

You can install these dependencies using `pip`:


```bash
pip install pymupdf pillow opencv-python-headless pytesseract numpy

```
## Notes
- Feel free to change the language, Tesseract OCR supports a lot of languges , you can find them here https://tesseract-ocr.github.io/tessdoc/Data-Files-in-different-versions.html

- The more you increase the zoom factor the better the quality of the pictures be , and by that the accuracy of the ocr improve . but you should keep in mind that that will also increase the needed time to run the code and get the wanted results . 

- this code will Run much faster if you are using a GPU.
