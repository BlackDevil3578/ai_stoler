"# streamlit_app_convert_pdf_to_images_and_text" 
# TEXT STOLER

TEXT STOLER is a Streamlit application designed to extract text from PDF files, convert it into various formats like Excel and PDF, and even compress extracted images into a ZIP file. This tool is ideal for users who want to retrieve text from PDF files, especially those containing embedded images.

## Features

- **PDF to Text Extraction**: Extracts text from uploaded PDF files.
- **Text to Excel Conversion**: Converts the extracted text into an Excel file, with each section grouped in chunks of 50 lines.
- **Text to PDF Conversion**: Creates a PDF file from the extracted text.
- **Image Compression**: Compresses images extracted from the PDF into a ZIP file.
- **Download Options**: Download the extracted text, Excel, PDF, and ZIP files directly from the app.
- **Integration with Other Apps**: Launches another Streamlit app directly from the interface.

## Prerequisites

- Python 3.x
- Streamlit
- FPDF
- pandas
- PyPDF2 (if required for `pdf_to_text_file`)
- zipfile
- tempfile
- subprocess
- DejaVuSansCondensed.ttf (for Unicode support in PDF creation)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/text-stoler.git
   cd text-stoler

2. Install the required Python packages:

pip install -r requirements.txt

3. Running the App
streamlit run main.py

4. Folder Structure
app.py: The main Streamlit application.
pdf_to_text_file.py: A Python script/module to handle PDF-to-text conversion.
requirements.txt: Contains the list of required Python packages.
README.md: Project documentation.
Usage
5. Text Extraction
Upload a PDF file to extract its text content.
The extracted text is displayed in a text area and saved as a .txt file.
6. Save as Excel
The text is automatically divided into sections (50 lines each) and saved as an Excel file.
Download the Excel file directly from the app.
7. Save as PDF
The extracted text is converted to a PDF file.
Download the newly created PDF file directly from the app.
8. Image Compression
If your PDF contains images, they are automatically extracted and compressed into a ZIP file.
Download the ZIP file directly from the app.
9. Integration with Other Apps
Click the button to launch another Streamlit app if additional features or treatments are needed.

10. License : 
This project is licensed under the MIT License - see the LICENSE file for details.


Acknowledgments
This app was developed with the help of the Streamlit community and open-source Python libraries.
Special thanks to the authors and contributors of the libraries used in this project.
