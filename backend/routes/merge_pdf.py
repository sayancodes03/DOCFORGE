from fastapi import APIRouter, UploadFile, File
from fastapi.responses import FileResponse
from services.merge_pdf import merge_pdfs
import os

router = APIRouter()

@router.post("/merge-pdf")
async def merge_pdf(files: list[UploadFile] = File(...)):
    os.makedirs("uploads", exist_ok=True)
    os.makedirs("outputs", exist_ok=True)

    pdf_paths = []

    for file in files:
        path = f"uploads/{file.filename}"

        with open(path, "wb") as f:
            f.write(await file.read())

        pdf_paths.append(path)

    output_path = "outputs/merged.pdf"

    merge_pdfs(pdf_paths, output_path)

    return FileResponse(
        output_path,
        media_type="application/pdf",
        filename="merged.pdf"
    )