import Image
from pytesseract import image_to_string

#Class ImageToText:

def load_image(image_path, output_path):
    data = image_to_string(Image.open(image_path))

    with open(output_path, "w") as text_file:
        text_file.write(data)

