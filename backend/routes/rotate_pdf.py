from fastapi import APIRouter, UploadFile, File, Form
from fastapi.responses import FileResponse
from services.rotate_pdf import rotate_pdf
import os

router = APIRouter()

@router.post("/rotate-pdf")
async def rotate_pdf_route(
    file: UploadFile = File(...),
    angle: int = Form(...)
):
    os.makedirs("uploads", exist_ok=True)
    os.makedirs("outputs", exist_ok=True)

    input_path = f"uploads/{file.filename}"

    with open(input_path, "wb") as f:
        f.write(await file.read())

    output_path = "outputs/rotated.pdf"

    rotate_pdf(
        input_path,
        output_path,
        angle
    )

    return FileResponse(
        output_path,
        media_type="application/pdf",
        filename="rotated.pdf"
    )