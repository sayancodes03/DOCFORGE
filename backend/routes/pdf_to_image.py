from fastapi import APIRouter, UploadFile, File
from fastapi.responses import FileResponse
from services.pdf_to_image import pdf_to_images

import os

router = APIRouter()

@router.post("/pdf-to-image")
async def convert_pdf_to_image(
    file: UploadFile = File(...)
):
    os.makedirs("uploads", exist_ok=True)
    os.makedirs("outputs", exist_ok=True)

    pdf_path = f"uploads/{file.filename}"

    with open(pdf_path, "wb") as f:
        f.write(await file.read())

    images = pdf_to_images(
        pdf_path,
        "outputs"
    )

    return FileResponse(
        images[0],
        media_type="image/png",
        filename="page_1.png"
    )