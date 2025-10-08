import os
from PIL import Image, ImageOps, ImageEnhance

# Paths
input_folder = "/Users/chaiyy/Desktop/Python Proj/Untitled Folder 1/AI Bill Splitter/Receipt dataset Large"
output_folder = "/Users/chaiyy/Desktop/Python Proj/Untitled Folder 1/AI Bill Splitter/Cleaned_Receipts"

# Create output folder if not exists
os.makedirs(output_folder, exist_ok=True)

# Process sequentially named files
for i in range(1000, 1200):  # Adjust range based on your filenames
    filename = f"{i}-receipt.jpg"  # Change extension if needed
    input_path = os.path.join(input_folder, filename)
    output_path = os.path.join(output_folder, f"{i}-processed.jpg")

    if os.path.exists(input_path):
        try:
            # Open and preprocess image
            image = Image.open(input_path)
            image = ImageOps.grayscale(image)  # Convert to grayscale
            image = image.resize((1024, 768))  # Resize to standard dimensions
            enhancer = ImageEnhance.Contrast(image)
            image = enhancer.enhance(2.0)  # Enhance contrast

            # Save processed image
            image.save(output_path)
            print(f"Processed and saved: {output_path}")
        except Exception as e:
            print(f"Error processing {input_path}: {e}")
    else:
        print(f"File not found: {input_path}")
