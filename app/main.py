"""
This module initializes the FastAPI application and includes the necessary routes.

Imports:
    FastAPI (from fastapi): The main FastAPI class to create an API.
    health (from app.routers): Health check routes.
    user (from app.routers): User-related routes.
    candidate (from app.routers): Candidate-related routes.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import health, message

app = FastAPI(
    title="Python Task Salem Abu Hassan",
    openapi_url="/openapi.json",
    docs_url="/docs/swagger",
    redoc_url="/docs/redoc"
)

# Enable CORS support
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",  # Local development
        "https://salemabuhassan.com"  # Production site
    ],
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods
    allow_headers=["*"]   # Allows all headers
)

app.include_router(health.router)
app.include_router(message.router)