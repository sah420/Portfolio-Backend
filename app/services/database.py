"""
This module sets up the asynchronous MongoDB client for database operations.

Imports:
    motor.motor_asyncio: Asynchronous MongoDB driver for Python.
    settings (from app.config): Configuration settings for the application.

Attributes:
    client (AsyncIOMotorClient): Asynchronous MongoDB client.
"""

from motor.motor_asyncio import AsyncIOMotorClient
from app.config import settings
from contextlib import asynccontextmanager

# Initialize a global variable for the client
client = None


async def connect_to_mongo():
    global client
    if not client:
        client = AsyncIOMotorClient(settings.mongodb_url, uuidRepresentation='standard')


@asynccontextmanager
async def get_database():
    global client
    if not client:
        await connect_to_mongo()
    try:
        yield client[settings.mongodb_db_name]
    finally:
        client = None
        pass
