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


from pydantic import BaseModel, Field, field_validator

class Category(BaseModel):
    name: str = Field(
        ...,
        title="Category Name",
        description="The name of the category.",
        min_length=1,
        max_length=50, 
        pattern=r"^[\w-]+$",
        examples=["Phones", "Laptops"]
    )
    description: str = Field(
        ...,
        title="Category Description",
        description="The description of the category.",
        min_length=1,
        max_length=255
    )

class Product(BaseModel):
    name: str = Field(
        ...,
        title="Product Name",
        description="The name of the product.",
        min_length=1,
        max_length=50, 
        pattern=r"^[\w-]+$",
        examples=["Samsung", "iPhone"]
    )
    description: str = Field(
        ...,
        title="Product Description",
        description="The description of the product.",
        min_length=1,
        max_length=255
    )
    price: float = Field(
        ...,
        title="Product Price",
        description="The price of the product.",
        ge=0.0,
        lt=100000.0, 
        examples=[9.99, 19.99]
    )
    category: Category

    @field_validator('price', mode='before')
    @classmethod

    def price_check(cls, value: float) -> float:
        if round(value % 1, 2) != 0.99:
            raise ValueError("Price should end with '.99'")
        return value