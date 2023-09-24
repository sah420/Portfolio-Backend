"""
This module initializes the FastAPI application and includes the necessary routes.

Imports:
    FastAPI (from fastapi): The main FastAPI class to create an API.
    health (from app.routers): Health check routes.
    user (from app.routers): User-related routes.
    candidate (from app.routers): Candidate-related routes.
"""

from fastapi import FastAPI
from app.routers import health

app = FastAPI(
    title="Python Task Salem Abu Hassan",
    openapi_url="/openapi.json",
    docs_url="/docs/swagger",
    redoc_url="/docs/redoc"
)

app.include_router(health.router)
