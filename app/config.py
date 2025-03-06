from functools import lru_cache

from pydantic import EmailStr, Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Application configuration settings.

    This class defines the settings for the API, including administrative details,
    database connection parameters, and server configuration. Values can be loaded from
    environment variables, with a '.env' file serving as a source for these variables.
    """

    admin_email: EmailStr = Field(
        default="admin@example.com",
        title="Admin Email",
        description="The email address of the API administrator.",
    )
    mongodb_url: str = Field(
        default="mongodb://localhost:27017",
        title="MongoDB URL",
        description="The URL of the MongoDB database.",
    )
    db_name: str = Field(
        default="test_db",
        title="Database Name",
        description="The name of the database.",
    )
    secrete_key: str = Field(
        default="secret",
        title="Secrete Key",
        description="The secrete key of the API.",
    )
    origins: str = "*"  # Allowed origins for CORS configuration.
    host: str = "0.0.0.0"  # Server binding IP address.
    port: int = 9000  # Port on which the server will run.
    reload: bool = True  # Flag for auto-reload during development.
    model_config = SettingsConfigDict(
        env_file=".env"
    )  # Configuration to load settings from a .env file.


@lru_cache()
def get_settings() -> Settings:
    """
    Retrieve a cached instance of the application settings.

    This function uses an LRU (Least Recently Used) cache to ensure that the settings
    are only instantiated once. Subsequent calls will return the cached instance,
    reducing redundant processing.

    Returns:
        Settings: The application configuration settings.
    """
    return Settings()
