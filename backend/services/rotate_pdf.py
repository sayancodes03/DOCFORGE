from pypdf import PdfReader, PdfWriter

def rotate_pdf(input_pdf, output_pdf, angle):
    reader = PdfReader(input_pdf)
    writer = PdfWriter()

    for page in reader.pages:
        page.rotate(angle)
        writer.add_page(page)

    with open(output_pdf, "wb") as f:
        writer.write(f)