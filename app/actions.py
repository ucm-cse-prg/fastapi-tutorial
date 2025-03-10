import typing
from functools import wraps

from app.exceptions import InternalServerError


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
