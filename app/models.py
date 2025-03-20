"""
Module for defining Pydantic models for the application.

This module defines the data models for Product and Category, which are used
to validate and serialize the data passed between the API client and the server.
"""

# CHALLENGE:
# Remove any existing implementations.
# Your task is to define the Pydantic models representing your data.
#
# Requirements:
# - Define a Category model with fields like name and description.
# - Define a Product model with fields such as name, description, price, and category.
# - Price should be a positive number less than 100000, and ending in ".99", i.e., 9.99, 19.99, etc.
#
# Ensure you use proper data validation and type annotations.
#
# Example:
#
# from pydantic import BaseModel
#
# class Category(BaseModel):
#     # TODO: Define fields and validations for a product category
#     pass
#
# class Product(BaseModel):
#     # TODO: Define fields and validations for a product
#     pass

from pydantic import BaseModel, Field

class Category(BaseModel):
    """
    Data class representing a category of a product

    Attributes:
        name - name of a category
        description - description of a category
    """
    name: str = Field(
        title="Name",
        min_length=2,
        max_length=25,
    )

    description: str = Field(
        title="Description", 
        max_length=120,
    )

class Product(BaseModel):
    """
    Data class representing a type of product

    Attributes:
        name (str) - name of product
        description (str)-  short description of a product
        price (float) - the price of a product; greater than 0 and less than 100000
        category (Category) - the category of a product
    """

    name: str = Field(
        title="Name",
        min_length=2,
        max_length=25
    )

    description: str = Field(
        title="Description", 
        max_length=100,

    )

    price: float = Field(
        title="Price",
        lt=100000,
        gt=0, 
    )

    category: Category
