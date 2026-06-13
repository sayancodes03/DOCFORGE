from PIL import Image

def convert_image_to_pdf(image_path, pdf_path):
    image = Image.open(image_path)

    if image.mode != "RGB":
        image = image.convert("RGB")

    image.save(pdf_path, "PDF")