import fitz

def compress_pdf(input_path, output_path):
    pdf = fitz.open(input_path)

    pdf.save(
        output_path,
        garbage=4,
        deflate=True,
        clean=True
    )

    pdf.close()