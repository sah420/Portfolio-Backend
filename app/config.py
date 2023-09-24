"""
This module sets up the project configuration using Pydantic and dotenv.

Imports:
    BaseSettings (from pydantic_settings): Base class for Pydantic settings.
    load_dotenv (from dotenv): Function to load environment variables.
    os: Module to interact with the operating system.
"""

from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os

load_dotenv()


class Settings(BaseSettings):
    """Configuration settings for the application."""
    mongodb_url: str = os.getenv("DATABASE_URI")
    mongodb_db_name: str = "python_task_salem_abuhassan"


settings = Settings()
