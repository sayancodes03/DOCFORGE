from fastapi import APIRouter, UploadFile, File
from fastapi.responses import FileResponse
from services.image_to_pdf import convert_image_to_pdf
import os

router = APIRouter()

@router.post("/image-to-pdf")
async def image_to_pdf(file: UploadFile = File(...)):
    
    os.makedirs("uploads", exist_ok=True)
    os.makedirs("outputs", exist_ok=True)

    image_path = f"uploads/{file.filename}"

    with open(image_path, "wb") as f:
        f.write(await file.read())

    pdf_path = f"outputs/{file.filename}.pdf"

    convert_image_to_pdf(image_path, pdf_path)

    return FileResponse(
        pdf_path,
        media_type="application/pdf",
        filename="converted.pdf"
    )