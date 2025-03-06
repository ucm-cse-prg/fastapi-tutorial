"""
Module for testing product-related API endpoints.

This module includes tests for creating, retrieving, updating, and deleting products.
Each test function interacts with the API endpoints and asserts the expected responses.
"""

import pytest
from beanie import PydanticObjectId
from faker import Faker
from httpx import AsyncClient
from pydantic import BaseModel

fake = Faker()

pytestmark = pytest.mark.asyncio


# Test Category model using Pydantic
@pytest.mark.skip()
class TestCategory(BaseModel):
    """
    Data model representing a product category for testing.

    Attributes:
        name (str): The name of the category.
        description (str): A description of the category.
    """

    name: str = fake.word()
    description: str = fake.sentence()


# Product model using Pydantic
@pytest.mark.skip()
class TestProduct(BaseModel):
    """
    Data model representing a product for testing.

    Attributes:
        id (PydanticObjectId or None): The unique identifier for the product.
        name (str): The name of the product.
        price (float): The price of the product.
        description (str): A description of the product.
        category (TestCategory): The category of the product.
    """

    id: PydanticObjectId | None = None
    name: str = fake.word()
    price: float = fake.random_number(2) + 0.99
    description: str = fake.sentence()
    category: TestCategory = TestCategory()


# Create a new product instance to be reused across tests
new_product = TestProduct()


async def test_create_product(
    client_test: AsyncClient, new_product: TestProduct = new_product
):
    """
    Test for creating a new product.

    This test sends a POST request with product data to create a new product.
    It asserts that the API returns a status code 201 and that the returned data matches the sent payload.

    Returns:
        TestProduct: The newly created product with its assigned ID.
    """
    print("\n")
    print("Creating new product: ", new_product.name)
    # Send POST request to create the product
    response = await client_test.post("/products/", json=new_product.model_dump())
    # Assert that the product is created successfully
    assert response.status_code == 201
    response = response.json()
    # Validate returned fields
    assert response.get("id") is not None
    assert response.get("name") == new_product.name
    assert response.get("price") == new_product.price
    assert response.get("description") == new_product.description
    new_product.id = response.get("id")
    print(
        "New product has been created: ", new_product.name, "with id: ", new_product.id
    )
    return new_product


async def test_get_product(
    client_test: AsyncClient, new_product: TestProduct = new_product
):
    """
    Test for retrieving a product.

    This test sends a GET request to fetch the product by its id.
    It validates that the API returns the product with the correct data.

    Returns:
        TestProduct: The retrieved product.
    """
    print("\n")
    print("Getting product: ", new_product.name)
    # Send GET request to retrieve the product
    response = await client_test.get(f"/products/{new_product.id}")
    assert response.status_code == 200
    response = response.json()
    # Validate returned fields
    assert response.get("id") == new_product.id
    assert response.get("name") == new_product.name
    assert response.get("price") == new_product.price
    assert response.get("description") == new_product.description
    print("Product has been retrieved: ", new_product.name)
    return new_product


async def test_update_product(
    client_test: AsyncClient, new_product: TestProduct = new_product
):
    """
    Test for updating an existing product.

    This test sends a PATCH request with updated product data.
    It asserts that the API returns status 200 and that the returned data reflects the updates.

    Returns:
        TestProduct: The updated product.
    """
    print("\n")
    print("Updating product: ", new_product.name)
    # Generate new data for the update
    new_name = fake.word()
    new_description = fake.sentence()
    new_price = fake.random_number(2) + 0.99
    # Send PATCH request to update the product
    response = await client_test.patch(
        f"/products/{new_product.id}",
        json={
            "name": new_name,
            "description": new_description,
            "price": new_price,
        },
    )
    assert response.status_code == 200
    response = response.json()
    # Validate updated fields
    assert response.get("id") == new_product.id
    assert response.get("name") == new_name
    assert response.get("price") == new_price
    assert response.get("description") == new_description
    # Update local product instance data
    new_product.name = new_name
    new_product.description = new_description
    new_product.price = new_price
    print("Product has been updated: ", new_product.name)
    return new_product


async def test_create_product_invalid_price_low(client_test: AsyncClient):
    """
    Test for creating a product with a price below the valid threshold.

    Expects a 422 status code due to validation error.
    """
    invalid_product = {
        "name": "ValidName",
        "description": "Valid product description",
        "price": -5.0,  # Invalid: less than 0
        "category": {"name": "Phones", "description": "Mobile phones"},
    }
    # Send POST request with invalid price
    response = await client_test.post("/products/", json=invalid_product)
    assert response.status_code == 422


async def test_create_product_invalid_price_high(client_test: AsyncClient):
    """
    Test for creating a product with a price above the valid threshold.

    Expects a 422 status code due to validation error.
    """
    invalid_product = {
        "name": "ValidName",
        "description": "Valid product description",
        "price": 100001,  # Invalid: greater than allowed
        "category": {"name": "Phones", "description": "Mobile phones"},
    }
    # Send POST request with invalid price
    response = await client_test.post("/products/", json=invalid_product)
    assert response.status_code == 422


async def test_create_product_invalid_name(client_test: AsyncClient):
    """
    Test for creating a product with an invalid name.

    The name includes spaces and violates the expected regex pattern.
    Expects a 422 status code due to validation error.
    """
    invalid_product = {
        "name": "Invalid Name",  # Contains a space, violating the regex
        "description": "Valid product description",
        "price": 999.99,
        "category": {"name": "Phones", "description": "Mobile phones"},
    }
    # Send POST request with invalid name
    response = await client_test.post("/products/", json=invalid_product)
    assert response.status_code == 422


async def test_update_product_invalid_data(
    client_test: AsyncClient, new_product: TestProduct = new_product
):
    """
    Test for updating a product with invalid data.

    This test uses invalid update data (name with spaces and negative price)
    and expects a 422 status code.
    """
    invalid_update = {
        "name": "Invalid Name",  # Invalid: name contains space
        "description": "Updated description",
        "price": -20.0,  # Invalid: negative price
    }
    # Send PATCH request with invalid update data
    response = await client_test.patch(
        f"/products/{new_product.id}", json=invalid_update
    )
    assert response.status_code == 422


async def test_delete_product(
    client_test: AsyncClient, new_product: TestProduct = new_product
):
    """
    Test for deleting a product.

    This test sends a DELETE request for the specified product
    and asserts that the API returns status code 204 indicating successful deletion.

    Returns:
        TestProduct: The product that was deleted.
    """
    print("\n")
    print("Deleting product: ", new_product.name)
    # Send DELETE request to remove the product
    response = await client_test.delete(f"/products/{new_product.id}")
    assert response.status_code == 204
    print("Product has been deleted: ", new_product.name)
    return new_product
