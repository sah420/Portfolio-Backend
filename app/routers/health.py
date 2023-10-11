"""
This module sets up the route for health checking.

Imports:
    APIRouter (from fastapi): FastAPI utility for routing.

Routes:
    GET /health: Returns a health check response.

"""

from fastapi import APIRouter

router = APIRouter()


@router.get("/", tags=["default"])
async def default_page():
    return {"Status": "Backend running successfully."}


@router.get("/health", tags=["health"])
async def health_check():
    """
    Endpoint to check the health of the service.

    Returns:
        dict: A dictionary indicating the health status.
    """
    return {"Status": "Okay"}

