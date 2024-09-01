import streamlit as st
import pdf_to_text_file
import tempfile
import os
import pandas as pd
from fpdf import FPDF
import subprocess
import zipfile

# Initialize session state for download trigger
if 'download_triggered' not in st.session_state:
    st.session_state.download_triggered = False


def save_text_to_excel(text_file, excel_file):
    with open(text_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # Group the text into chunks of 50 lines
    rows = [''.join(lines[i:i + 50]) for i in range(0, len(lines), 50)]

    # Create a DataFrame
    df = pd.DataFrame(rows, columns=['Text'])
    df['Section'] = range(1, len(df) + 1)
    # Save DataFrame to Excel
    df.to_excel(excel_file, index=False)

    return df


def compress_folder_to_zip(folder_path, zip_file):
    with zipfile.ZipFile(zip_file, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, _, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, folder_path)
                zipf.write(file_path, arcname=arcname)


def save_text_to_pdf(text_file, pdf_file):
    pdf = FPDF(orientation='P', unit='mm', format='A4')
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    # Use a font that supports Unicode
    pdf.add_font('DejaVu', '', 'DejaVuSansCondensed.ttf', uni=True)
    pdf.set_font('DejaVu', '', 12)

    with open(text_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    for line in lines:
        pdf.multi_cell(0, 10, line)

    pdf.output(pdf_file)


# Display header for the file uploader
st.markdown("<h1 style='color: #AAFF00;'>TEXT STOLER :</h1>", unsafe_allow_html=True)
st.markdown(
    "<h6 style='color: #C0C0C0;'>Reveal text from any PDF, no matter if it's nestled in images.<br><br> Your best way to steal all the text from pdf files . </h6>",
    unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<h4 style='color: #AAFF00;'>CHOOSE A PDF FILE :</h4>", unsafe_allow_html=True)

# File uploader widget
uploaded_file = st.file_uploader("Upload PDF", type='pdf')

if uploaded_file is not None and not st.session_state.download_triggered:
    base_name = os.path.splitext(os.path.basename(uploaded_file.name))[0]
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:
        temp_file.write(uploaded_file.read())
        temp_file_path = temp_file.name

    pdf_to_text_file.main(temp_file_path, base_name)

    output_text_file = temp_file_path.replace('.pdf', '.txt')
    output_excel_file = temp_file_path.replace('.pdf', '.xlsx')
    output_pdf_file = temp_file_path.replace('.pdf', '_extracted.pdf')

    # Save text to Excel
    df = save_text_to_excel(output_text_file, output_excel_file)

    # Save text to PDF
    save_text_to_pdf(output_text_file, output_pdf_file)

    # Assuming `base_name` is the name of the PDF file without the extension
    image_folder = f"C:\\Users\\Aymen\\Desktop\\appPDFtreatment\\{base_name}_images"

    # Ensure that the image folder exists and contains files
    if os.path.exists(image_folder) and os.listdir(image_folder):
        output_zip_file = os.path.join(tempfile.gettempdir(), f"{base_name}_images.zip")

        # Compress the existing image folder into a ZIP file
        compress_folder_to_zip(image_folder, output_zip_file)

        # Add download button for the ZIP file
        with open(output_zip_file, 'rb') as file:
            if st.download_button(
                    label="Download Images as ZIP",
                    data=file,
                    file_name=f"{base_name}_images.zip",
                    mime="application/zip"
            ):
                st.session_state.download_triggered = True
    else:
        st.warning("No images were found to compress into a ZIP file.")

    # Display the DataFrame in Streamlit in a 2-column layout
    col1, col2 = st.columns(2)
    with col1:
        st.text_area("Extracted text:", open(output_text_file, 'r', encoding='utf-8').read(), height=400)
        # Add download button for the text file
        with open(output_text_file, 'rb') as file:
            if st.download_button(
                    label="Download Text File",
                    data=file,
                    file_name=f"{base_name}.txt",
                    mime="text/plain"
            ):
                st.session_state.download_triggered = True

        # Add download button for the PDF file
        with open(output_pdf_file, 'rb') as file:
            if st.download_button(
                    label="Download PDF File",
                    data=file,
                    file_name=f"{base_name}_extracted.pdf",
                    mime="application/pdf"
            ):
                st.session_state.download_triggered = True

    with col2:
        st.markdown("<h6 style='color: white;'>Excel file :</h6>", unsafe_allow_html=True)
        st.dataframe(df)
        # Add download button for the Excel file
        with open(output_excel_file, 'rb') as file:
            if st.download_button(
                    label="Download Excel File",
                    data=file,
                    file_name=f"{base_name}.xlsx",
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            ):
                st.session_state.download_triggered = True

st.markdown("<h6 style='color: white;'>For more treatments and features, please visit:</h6>", unsafe_allow_html=True)

# Hyperlink to the other app (replace the URL with the actual link to your other app)
if st.button("Go to the other app"):
    subprocess.Popen(
        ['streamlit', 'run', 'C:\\Users\\Aymen\\PycharmProjects\\pdf to excel and text\\main.py', '--server.port',
         '8502'])
    st.markdown('Our other app is now running on [http://localhost:8502](http://localhost:8502)',
                unsafe_allow_html=True)

# Reset the trigger after the script runs so it doesn't affect future interactions
st.session_state.download_triggered = False
