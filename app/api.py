from fastapi import APIRouter

router = APIRouter()

# CHALLENGE:
# Remove any working CRUD implementations.
# Your task is to implement the following API endpoints using the Pydantic schemas,
# Beanie documents, and actions that you will build:
#
# - GET /products/      -> Retrieve all products.
# - GET /products/{id}  -> Retrieve a product by ID.
# - POST /products/     -> Create a new product.
# - PATCH /products/{id} -> Update an existing product.
# - DELETE /products/{id} -> Delete a product.
#
# For each endpoint:
# - Validate the incoming data using your custom Pydantic schemas.
# - Delegate business logic to functions in the actions module.
# - Return appropriate responses and status codes.
#
# Example (for guidance):
#
# @router.post("/", response_model=YourCreateProductResponseSchema, status_code=201)
# async def create_product_endpoint(product: YourCreateProductRequestSchema):
#     # TODO: Implement creation logic using your actions function
#     pass
