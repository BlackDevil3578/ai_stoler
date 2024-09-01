import cv2
import pytesseract
from PIL import Image, ImageEnhance, ImageFilter
import numpy as np
import os

# Path to your Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Update this path if needed

Image.MAX_IMAGE_PIXELS = None

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
    text = pytesseract.image_to_string(open_cv_image, lang='eng')

    return text

def save_text_to_file(folder_name, text_data):
    file_path = os.path.join(folder_name + ".txt")
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(text_data)

def process_images_in_folder(folder_path):
    files = [f for f in os.listdir(folder_path) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif'))]
    files.sort(key=lambda f: int(''.join(filter(str.isdigit, f))) if any(char.isdigit() for char in f) else float('inf'))

    folder_name = os.path.basename(folder_path)
    text_data = ""

    for index, filename in enumerate(files):
        image_path = os.path.join(folder_path, filename)
        print(f"Processing {filename}...")
        preprocessed_image = preprocess_image(image_path)
        if preprocessed_image is not None:
            text = extract_text_from_image(preprocessed_image)
            text_data += f"page {index + 1}:\n{text}\n{'-' * 50}\n"

    save_text_to_file(folder_name, text_data)

if __name__ == "__main__":
    folder_path = r'y_images'  # Replace with your folder path

    # Process all images in the folder
    process_images_in_folder(folder_path)
