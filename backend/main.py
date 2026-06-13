from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.image_to_pdf import router as image_router

app = FastAPI(
    title="DocForge API",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(image_router)

@app.get("/")
def home():
    return {
        "message": "DocForge API Running"
    }