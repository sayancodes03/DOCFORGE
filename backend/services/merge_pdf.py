from pypdf import PdfReader, PdfWriter

def merge_pdfs(pdf_files, output_path):
    writer = PdfWriter()

    for pdf_file in pdf_files:
        reader = PdfReader(pdf_file)

        for page in reader.pages:
            writer.add_page(page)

    with open(output_path, "wb") as output:
        writer.write(output)