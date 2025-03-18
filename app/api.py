from fastapi import APIRouter, HTTPException
from app.schemas import CreateProductRequest, CreateProductResponse, GetProductResponse, UpdateProductRequest, UpdateProductResponse, GetAllProductsResponse
from app.actions import create_product, get_all_products, update_product, delete_product, get_product
from app.documents import ProductDocument
from beanie import PydanticObjectId

import app.exceptions as exceptions

from typing import Literal, Optional

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

@router.post("/", response_model=CreateProductResponse, status_code=201)
async def create_product_endpoint(product: CreateProductRequest) -> ProductDocument:
    try:
        return await create_product(**product.model_dump())
    except exceptions.ProductNotFound as e:
        raise HTTPException(
            status_code=e.code,
            detail=e.detail
        )

@router.get("/", response_model=GetAllProductsResponse, status_code=200)
async def get_all_products_endpoint() -> dict[Literal['products'], list[ProductDocument]]:
    try:
        products: list[ProductDocument] = await get_all_products()
        return {"products": products}
    except exceptions.InternalServerError as e:
        raise HTTPException(
            status_code=e.code,
            detail=e.detail
        )

@router.get("/{product_id}", response_model=GetProductResponse, status_code=200)
async def get_product_endpoint(product_id: PydanticObjectId) -> ProductDocument:
        return await get_product(product_id)
    

@router.patch("/{product_id}", response_model=UpdateProductResponse, status_code=200)
async def update_product_endpoint(request_body: UpdateProductRequest, product: ProductDocument ) -> ProductDocument:
    try:
        return await update_product(product, **request_body.model_dump())
    except exceptions.ProductNotFound as e:
        raise HTTPException(
            status_code=e.code,
            detail=e.detail
        )

@router.delete("/{product_id}", status_code=204)
async def delete_product_endpoint(product: ProductDocument) -> None:
    try:
        await delete_product(product)
        return None
    except exceptions.ProductNotFound as e:
        raise HTTPException(
            status_code=e.code,
            detail=e.detail
        )