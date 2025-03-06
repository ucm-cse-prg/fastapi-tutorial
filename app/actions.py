from typing import Optional

from beanie import PydanticObjectId

from app.dependencies import product_dependency as get_product_by_id
from app.documents import Product
from app.exceptions import InternalServerError
from app.models import Category


# List all products
async def get_all_products() -> list[Product]:
    products: list[Product] = await Product.find_all().to_list()
    return products


# Get a single product
async def get_product(product_id: PydanticObjectId) -> Product:
    """Get a single product by ID.

    Args:
        product_id (PydanticObjectId): The ID of the product to get.

    Raises:
        ProductNotFound: If the product is not found.

    Returns:
        Product: The product if found.
    """

    # Get the product by ID
    return await get_product_by_id(product_id)


# Create a new product
async def create_product(
    name: str,
    price: float,
    category: Category,
    description: str = "",
) -> Product:
    new_product: Product = await Product(
        name=name, description=description, price=price, category=category
    ).insert()

    if not new_product:
        raise InternalServerError("Failed to create product")

    return new_product


# Update a product
async def update_product(
    product: Product,
    name: Optional[str] = None,
    description: Optional[str] = None,
    price: Optional[float] = None,
    category: Optional[Category] = None,
) -> Product:
    if name:
        product.name = name
    if description:
        product.description = description
    if price:
        product.price = price
    if category:
        product.category = category

    # Update the product
    await product.save()

    if not product:
        raise InternalServerError("Failed to update product")

    return product


async def delete_product(product: Product) -> None:
    """Delete a product

    Args:
        product (Product): The Product document to delete

    Raises:
        InternalServerError: If the product was not deleted
    """
    await Product.delete(product)

    if await Product.get(product.id):
        raise InternalServerError("Failed to delete product")
