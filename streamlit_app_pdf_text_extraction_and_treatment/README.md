# PDF-stoler

**PDF-stoler** is a Streamlit-based web application designed to facilitate the extraction, manipulation, and analysis of text from PDF files. The application allows users to upload PDF files, view and edit the extracted content in tabular form, and perform text analysis such as word counting and frequency distribution. Users can also download the processed data in Excel, text, and SQL formats.

## Features

- **Upload PDF Files**: Upload PDF files for text extraction.
- **Text Extraction**: Extract text from each page of the PDF and store it in an Excel file.
- **Page Numbering**: Optionally include page numbers in the extracted text.
- **Custom Text Splitting**: Split text based on specific start and end words.
- **Data Editing**: Insert, delete, or modify content for any page directly within the app.
- **Text Analysis**:
  - Count total words.
  - Count occurrences of specific words.
  - Display and download the frequency distribution of the top 10 most common words.
- **Data Export**: Download the processed data as an Excel file, text file, or SQL script.

## Requirements

Before running the application, ensure you have the following installed:

- Python 3.7+
- Streamlit
- pandas
- xlsxwriter
- PyPDF2
- pdfplumber
- matplotlib
- NLTK
- numpy
- python-docx

## Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/yourusername/pdf-stoler.git
   cd pdf-stoler



2. **Install dependencies**:

pip install -r requirements.txt


3. **Run the application**:

streamlit run app.py

4. **Upload a PDF file**:

Choose a PDF file to upload.
Select options for extracting text, including whether to include page numbers or split by specific words.

Process the content:

View and manipulate the extracted text and data in a DataFrame.
Perform word frequency analysis and other text processing tasks.

Download the results:

Export data as Excel, SQL, or plain text files.

**Acknowledgments**

This project uses the following open-source libraries:

. Streamlit
. Pandas
. PyPDF2
. pdfplumber
. Matplotlib
. NLTK
. NumPy
. python-docx

