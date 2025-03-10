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
