"""
Module for defining API request and response schemas.

This module defines Pydantic models that represent the data structures for products
used in various API endpoints, such as creating, retrieving, and updating products.
These schemas help with data validation and serialization between the client and server.
"""

from typing import Optional

from beanie import PydanticObjectId
from pydantic import BaseModel, Field

from app.models import Category, Product


class GetProductResponse(Product, BaseModel):
    """
    Schema for returning a single product.

    Inherits from Product model and adds an 'id' field.
    This schema is used for the response of the GET Product/{id} endpoint.
    """

    id: PydanticObjectId  # Unique identifier for the product


class GetAllProductsResponse(BaseModel):
    """
    Schema for returning all products.

    Contains a list of products represented by GetProductResponse.
    This schema is used for the response of the GET Products endpoint.
    """

    products: list[GetProductResponse]  # List of product responses


class CreateProductRequest(Product, BaseModel):
    """
    Schema for creating a new product.

    Inherits from the Product model.
    This schema is used for the request payload of the POST Product endpoint.
    """

    pass


class CreateProductResponse(Product, BaseModel):
    """
    Schema for returning the newly created product.

    Inherits from the Product model and includes an additional 'id' field.
    This schema is used for the response of the POST Product endpoint.
    """

    id: PydanticObjectId  # Unique identifier for the newly created product


class UpdateProductRequest(BaseModel):
    """
    Schema for updating an existing product.

    This schema defines the fields that can be updated for a product.
    All fields are optional since updates may target one or more attributes.
    This schema is used for the request payload of the PUT Product/{id} endpoint.
    """

    name: Optional[str] = Field(
        default=None,
        title="Name",
        description="Name of the product",
        max_length=20,
        min_length=2,
        pattern=r"^[\w-]+$",
        examples=["SM-G973F", "iPhone 12"],
    )
    description: Optional[str] = Field(
        default=None,
        title="Description",
        description="Description of the product",
        max_length=100,
        examples=["Samsung Galaxy S10", "The latest iPhone"],
    )
    price: Optional[float] = Field(
        default=None,
        title="Price",
        description="Price of the product",
        gt=0,
        lt=100000,
        allow_inf_nan=False,
        examples=[799.99, 1299.99],
    )
    category: Optional[Category] = None  # Optional updated category of the product


class UpdateProductResponse(GetProductResponse, BaseModel):
    """
    Schema for returning the updated product.

    Inherits from GetProductResponse which includes all product details along with the 'id'.
    This schema is used for the response of the PUT Product/{id} endpoint.
    """

    pass
