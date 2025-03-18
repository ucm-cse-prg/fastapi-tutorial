import typing 
from typing import Optional
from functools import wraps

from app.exceptions import InternalServerError

from app.documents import ProductDocument
from beanie import PydanticObjectId
from app.models import Category
from app.dependencies import get_product_by_id


# Wrapper function to run action and rais InternalServerError if it fails
@typing.no_type_check
def run_action(action):
    @wraps(action)
    async def wrapper(*args, **kwargs):
        try:
            # Call the wrapped function with provided arguments.
            return await action(*args, **kwargs)
        except Exception as e:
            # Convert APIException into HTTPException with corresponding code and message.
            raise InternalServerError(str(e))

    return wrapper


# CHALLENGE:
# Remove the existing CRUD business logic.
# Your task is to implement the action functions that will perform the following:
#
# - Create a new product:
#     * Validate inputs.
#     * Insert the new product into the MongoDB collection using Beanie.
# - Retrieve products:
#     * Get all products or a specific product by ID.
# - Update an existing product:
#     * Apply changes to the product object.
#     * Save the updated product to the database.
# - Delete a product:
#     * Remove the product document from the database.
#
# Define functions like create_product, get_product, update_product, delete_product with appropriate signatures.
#
# Example:
#
# async def create_product(name: str, price: float, category: YourCategoryType, description: str = "") -> YourProductType:
#     # TODO: Implement creation logic
#     pass

@run_action
async def get_all_products() -> list[ProductDocument]:
    all_products: ProductDocument = await ProductDocument.all().to_list()
    return all_products

async def create_product(name: str, price: float, category: str, description: str = "") -> ProductDocument:
    price = ProductDocument.price_check(price)
    
    new_product: ProductDocument = await ProductDocument(
        name=name,
        price=price,
        category=category,
        description=description
    ).insert()
    
    if not new_product:
        raise InternalServerError("Failed to create product.")

    return new_product

async def get_product(product_id: PydanticObjectId) -> ProductDocument:
    return await get_product_by_id(product_id)

async def update_product(product: ProductDocument, name: Optional[str], price: Optional[float], category: Optional[Category], description: Optional[str]) -> ProductDocument:
    if name: 
        product.name = name
    if price:
        product.price = price
    if category:
        product.category = category
    if description:
        product.description = description
    await product.save()

    return product

async def delete_product(product: ProductDocument) -> None:
    await product.delete()