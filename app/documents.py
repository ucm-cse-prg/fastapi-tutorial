"""
Module for defining database document models.

This module uses Beanie's Document base class combined with Pydantic models
to define the schema of documents stored in the MongoDB collection.
"""

from beanie import Document

from app.models import Product as ProductModel


class Product(Document, ProductModel):
    """
    Database document for a Product.

    This class inherits from Beanie's Document to facilitate MongoDB operations,
    and from ProductModel for the product schema definition.
    """

    class Settings:
        """
        Beanie settings for the Product document.

        Specifies the MongoDB collection name where Product documents are stored.
        """

        name = "products"
