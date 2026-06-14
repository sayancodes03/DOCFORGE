# Import FastAPI framework
from fastapi import FastAPI

# Import CORS middleware so frontend can talk to backend
from fastapi.middleware.cors import CORSMiddleware

# Import Image -> PDF routes
from routes.image_to_pdf import router as image_router

# Import Merge PDF routes
from routes.merge_pdf import router as merge_router

from routes.split_pdf import router as split_router

from routes.pdf_to_image import router as pdf_to_image_router

# Create FastAPI application
app = FastAPI(
    title="DocForge API",
    version="1.0.0"
)


# Allow requests from Next.js frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000"
    ],  # Frontend URL
    allow_credentials=True,
    allow_methods=["*"],  # Allow GET, POST, PUT, DELETE, etc.
    allow_headers=["*"],  # Allow all headers
)


# Register Image -> PDF endpoints
app.include_router(image_router)

# Register Merge PDF endpoints
app.include_router(merge_router)

app.include_router(split_router)
app.include_router(pdf_to_image_router)

# Health check endpoint
@app.get("/")
def home():
    return {
        "message": "DocForge API Running"
    }