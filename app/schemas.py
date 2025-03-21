"""
Module for defining API request and response schemas.

This module defines Pydantic models that represent the data structures for products
used in various API endpoints, such as creating, retrieving, and updating products.
These schemas help with data validation and serialization between the client and server.
"""

from typing import Optional

from beanie import PydanticObjectId
from pydantic import BaseModel

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


class CreateProductResponse(GetProductResponse, BaseModel):
    """
    Schema for returning the newly created product.

    Inherits from the GetProductResponse model to include an additional 'id' field.
    This schema is used for the response of the POST Product endpoint.
    """

    pass


class UpdateProductRequest(Product, BaseModel):
    """
    Schema for updating an existing product.

    This schema defines the fields that can be updated for a product.
    All fields are optional since updates may target one or more attributes.
    This schema is used for the request payload of the PUT Product/{id} endpoint.
    """

    # NOTE: We are using the 'type: ignore' comment to suppress mypy errors.
    # We are overriding the fields from the Product model to make them optional
    # Due to the original fields being required, making them optional raises a mypy error
    # Hence, we use the 'type: ignore' comment to suppress the error

    name: Optional[str] = None  # type: ignore
    description: Optional[str] = None  # type: ignore
    price: Optional[float] = None  # type: ignore
    category: Optional[Category] = None  # type: ignore


class UpdateProductResponse(GetProductResponse, BaseModel):
    """
    Schema for returning the updated product.

    Inherits from GetProductResponse which includes all product details along with the 'id'.
    This schema is used for the response of the PUT Product/{id} endpoint.
    """

    pass
