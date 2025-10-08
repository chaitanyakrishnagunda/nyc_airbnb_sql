from PIL import Image
import pytesseract

# Path to the Tesseract executable
# Update this path with the installation directory
pytesseract.pytesseract.tesseract_cmd = r'/opt/homebrew/bin/tesseract'

# Load the sample bill image
image_path = "/Users/chaiyy/Desktop/Python Proj/Untitled Folder 1/AI Bill Splitter/Cleaned_Receipts/1000-processed.jpg"  # Replace with your image file path
image = Image.open(image_path)

# Perform OCR
extracted_text = pytesseract.image_to_string(image)

# Print the extracted text
print("Extracted Text:")
print(extracted_text)

import os
from PIL import Image
import pytesseract

# Path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'/opt/homebrew/bin/tesseract'

# Paths
input_folder = "/Users/chaiyy/Desktop/Python Proj/Untitled Folder 1/AI Bill Splitter/Cleaned_Receipts"
output_file = "/Users/chaiyy/Desktop/Python Proj/Untitled Folder 1/AI Bill Splitter/extracted_text.txt"

# Open output file for writing extracted text
with open(output_file, "w") as text_file:
    # Iterate over all files in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith("-processed.jpg"):  # Only process relevant files
            image_path = os.path.join(input_folder, filename)

            try:
                # Load and process the image
                image = Image.open(image_path)
                extracted_text = pytesseract.image_to_string(image)

                # Write the filename and extracted text to the file
                text_file.write(f"--- Extracted Text from {filename} ---\n")
                text_file.write(extracted_text + "\n\n")
                print(f"Text extracted from {filename}")
            except Exception as e:
                print(f"Error processing {filename}: {e}")

print(f"Extraction complete. Text saved to {output_file}")

#easyocr
import easyocr

reader = easyocr.Reader(['en'])
result = reader.readtext("/Users/chaiyy/Desktop/Python Proj/Untitled Folder 1/AI Bill Splitter/Cleaned_Receipts/1151-processed.jpg")

# Print detected text
for detection in result:
    print(detection[1])
