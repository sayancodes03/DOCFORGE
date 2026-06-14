from fastapi import APIRouter, UploadFile, File, Form
from fastapi.responses import FileResponse
from services.split_pdf import split_pdf
import os

router = APIRouter()

@router.post("/split-pdf")
async def split_pdf_route(
    file: UploadFile = File(...),
    start_page: int = Form(...),
    end_page: int = Form(...)
):
    os.makedirs("uploads", exist_ok=True)
    os.makedirs("outputs", exist_ok=True)

    pdf_path = f"uploads/{file.filename}"

    with open(pdf_path, "wb") as f:
        f.write(await file.read())

    output_path = "outputs/split.pdf"

    split_pdf(
        pdf_path,
        start_page,
        end_page,
        output_path
    )

    return FileResponse(
        output_path,
        media_type="application/pdf",
        filename="split.pdf"
    )