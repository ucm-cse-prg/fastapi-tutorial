"""
Module for initializing MongoDB connection and configuring Beanie ODM.

This module sets up the connection to the MongoDB database using Motor and initializes
Beanie with the application's document models.
"""

from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

from app.config import get_settings
from app.documents import Product

# Retrieve application settings which include MongoDB connection details.
SETTINGS = get_settings()


async def init_mongo() -> None:
    """
    Initialize the MongoDB connection and configure Beanie ODM.

    This function creates a Motor client using the MongoDB URL from the settings,
    selects the database specified in settings, and initializes Beanie with the document
    models (currently only the Product document). It should be called during application startup.

    Raises:
        Exception: If unable to connect to MongoDB or initialize Beanie.
    """

    print(SETTINGS.mongodb_url)
    print(SETTINGS.db_name)

    # Create a Motor client to interact with MongoDB.
    client: AsyncIOMotorClient = AsyncIOMotorClient(SETTINGS.mongodb_url)

    # Access the database using the name provided in the settings.
    db = client[SETTINGS.db_name]

    # Initialize Beanie with the database and the list of document models.
    await init_beanie(database=db, document_models=[Product])
