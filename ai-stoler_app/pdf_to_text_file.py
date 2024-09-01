import os
import fitz  # PyMuPDF
from PIL import Image, ImageEnhance, ImageFilter
import cv2
import pytesseract
import numpy as np

# Path to your Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Update this path if needed

Image.MAX_IMAGE_PIXELS = None

# defining the language of the extracted text and the zoom factor
lang='ara'
zoom_factor=2.0

def pdf_to_images(pdf_path, zoom_factor=32.0, output_folder=None, base_name="output_folder"):
    # Extract the base name of the PDF file (without extension)
    if output_folder is None:
        if base_name is None:
            base_name = os.path.splitext(os.path.basename(pdf_path))[0]
        output_folder = f"{base_name}_images"

    # Create the output folder named after the PDF file
    os.makedirs(output_folder, exist_ok=True)

    # Open the PDF file
    pdf_document = fitz.open(pdf_path)

    # Iterate over each page in the PDF
    for page_num in range(len(pdf_document)):
        # Select the page
        page = pdf_document.load_page(page_num)

        # Define the transformation matrix for higher resolution
        matrix = fitz.Matrix(zoom_factor, zoom_factor)

        # Render the page to a pixmap (image) with the specified matrix
        pix = page.get_pixmap(matrix=matrix, alpha=False)

        # Convert the pixmap to an image
        image = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)

        # Save the image
        image_path = os.path.join(output_folder, f"page_{page_num + 1}.png")
        image.save(image_path, format="PNG", optimize=True, quality=100)

    # Close the PDF file
    pdf_document.close()

    print(f"PDF pages saved as images in '{output_folder}'")
    return output_folder

def preprocess_image(image_path):
    try:
        # Open the image file
        image = Image.open(image_path)

        # Convert image to grayscale
        gray_image = image.convert('L')

        # Increase contrast
        enhancer = ImageEnhance.Contrast(gray_image)
        contrast_image = enhancer.enhance(2)  # Adjust contrast level as needed

        # Apply a filter to reduce noise
        filtered_image = contrast_image.filter(ImageFilter.MedianFilter())

        return filtered_image
    except Exception as e:
        print(f"Error processing image {image_path}: {e}")
        return None


def extract_text_from_image(image):
    # Convert PIL image to OpenCV format
    open_cv_image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

    # Perform OCR on the image
    text = pytesseract.image_to_string(open_cv_image, lang=lang)

    return text


def save_text_to_file(file_path, page_number, text_data):
    with open(file_path, 'a', encoding='utf-8') as file:
        # file.write(f"Page {page_number}:\n{text_data}\n{'-' * 50}\n")  # Commented line
        file.write(f"{text_data}\n")  # Without page index


def process_images_in_folder(folder_path, output_file):
    files = [f for f in os.listdir(folder_path) if
             f.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif'))]
    files.sort(
        key=lambda f: int(''.join(filter(str.isdigit, f))) if any(char.isdigit() for char in f) else float('inf'))

    text_data = ""  # Initialize text_data variable

    for index, filename in enumerate(files):
        image_path = os.path.join(folder_path, filename)
        print(f"Processing {filename}...")
        preprocessed_image = preprocess_image(image_path)
        if preprocessed_image is not None:
            text = extract_text_from_image(preprocessed_image)
            save_text_to_file(output_file, index + 1, text)
            # text_data += f"page {index + 1}:\n{text}\n{'-' * 50}\n"  # Commented line

    # Uncomment the next line to save the entire text_data to the file if needed
    # save_text_to_file(output_file, "All Pages", text_data)


def pdf_to_text(pdf_path, zoom_factor=32.0, output_folder=None, base_name="output_folder"):
    # Convert PDF to images with the provided or default folder name
    image_folder = pdf_to_images(pdf_path, zoom_factor, output_folder, base_name)

    # Define the output text file path
    output_file = os.path.splitext(pdf_path)[0] + ".txt"

    # Process images in the folder to extract text
    process_images_in_folder(image_folder, output_file)


def main(pdf_path, base_name=None):
    # Example usage
    try:
        pdf_to_text(pdf_path, zoom_factor=zoom_factor, base_name=base_name)
    except Exception as e:
        print(f"An error occurred: {e}")
        pdf_path += ".pdf"
        try:
            pdf_path = input("Give me your PDF file path: ")
            pdf_to_text(pdf_path, zoom_factor=zoom_factor, base_name=base_name)
        except Exception as e:
            print(f"An error occurred: {e}")
            print("There is no such file. Please double-check and re-run this code.")

if __name__ == '__main__':
    pdf_path = input("give me the path to your pdf file : ")
    main(pdf_path)