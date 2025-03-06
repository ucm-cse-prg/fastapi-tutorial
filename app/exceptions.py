from beanie import PydanticObjectId
from fastapi import status


class APIException(Exception):
    """
    Base exception class for API-related errors.

    This exception is raised when an API error occurs. It includes an HTTP status code
    and a descriptive error message.
    """

    def __init__(self, code: int, detail: str):
        # HTTP status code that indicates the type of error.
        self.code = code
        # A descriptive error message.
        self.detail = detail

    def __str__(self) -> str:
        # Print the error detail for logging purposes.
        print(self.detail)
        return self.detail


class InternalServerError(APIException):
    """
    Exception raised for internal server errors (HTTP 500).

    Inherits from APIException and automatically assigns a 500 HTTP status code.
    """

    def __init__(self, detail: str):
        # Initialize with HTTP 500 status code and a generic internal server error message.
        super().__init__(
            code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal Server Error"
        )


class BadRequest(APIException):
    """
    Exception raised for bad requests (HTTP 400).

    Inherits from APIException and automatically assigns a 400 HTTP status code.
    """

    def __init__(self, detail: str):
        # Initialize with HTTP 400 status code and a generic bad request message.
        super().__init__(code=status.HTTP_400_BAD_REQUEST, detail="Bad Request")


class NotFound(APIException):
    """
    Exception raised when a requested resource is not found (HTTP 404).

    Inherits from APIException and automatically assigns a 404 HTTP status code.
    """

    def __init__(self, detail: str):
        # Initialize with HTTP 404 status code and a generic not found message.
        super().__init__(code=status.HTTP_404_NOT_FOUND, detail="Not Found")


class ProductNotFound(APIException):
    """
    Exception raised when a product is not found in the database (HTTP 404).

    Inherits from APIException and provides a detailed message including the product ID.
    """

    def __init__(self, product_id: PydanticObjectId):
        # Initialize with HTTP 404 status code and a message specifying the missing product's ID.
        super().__init__(
            code=status.HTTP_404_NOT_FOUND,
            detail=f"Product with ID {product_id} not found",
        )
