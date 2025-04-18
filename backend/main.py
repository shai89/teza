from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pathlib import Path
from api.routes.submission import router as submission_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# API routes
app.include_router(submission_router)

frontend_path = Path(__file__).resolve().parent / "frontend_build"
app.mount("/", StaticFiles(directory=frontend_path, html=True), name="frontend")
