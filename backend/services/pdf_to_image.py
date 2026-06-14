import fitz
import os

def pdf_to_images(pdf_path, output_folder):
    pdf = fitz.open(pdf_path)

    image_paths = []

    for page_num in range(len(pdf)):
        page = pdf.load_page(page_num)

        pix = page.get_pixmap()

        image_path = os.path.join(
            output_folder,
            f"page_{page_num + 1}.png"
        )

        pix.save(image_path)

        image_paths.append(image_path)

    return image_paths