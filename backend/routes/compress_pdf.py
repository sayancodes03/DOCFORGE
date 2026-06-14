from fastapi import APIRouter, UploadFile, File
from fastapi.responses import FileResponse
from services.compress_pdf import compress_pdf
import os

router = APIRouter()

@router.post("/compress-pdf")
async def compress_pdf_route(
    file: UploadFile = File(...)
):
    os.makedirs("uploads", exist_ok=True)
    os.makedirs("outputs", exist_ok=True)

    input_path = f"uploads/{file.filename}"

    with open(input_path, "wb") as f:
        f.write(await file.read())

    output_path = "outputs/compressed.pdf"

    compress_pdf(
        input_path,
        output_path
    )

    return FileResponse(
        output_path,
        media_type="application/pdf",
        filename="compressed.pdf"
    )