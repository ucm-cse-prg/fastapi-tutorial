import typer
import uvicorn

# Create a Typer app instance for building command-line applications.
app = typer.Typer()


@app.command()
def start_server(
    host: str = "localhost",
    port: int = 8000,
    reload: bool = False,
    mongodb: str = "mongodb://localhost:27017",
) -> None:
    """
    Start the FastAPI server using uvicorn.

    This command starts the uvicorn server by referencing the FastAPI application
    defined in the app module. It accepts parameters for host, port, reload, and a MongoDB URL.
    Note: The 'mongodb' parameter is currently not utilized in this function.

    Args:
        host (str): The hostname to bind the server to. Defaults to "localhost".
        port (int): The port on which to run the server. Defaults to 8000.
        reload (bool): If True, enables auto-reload for development. Defaults to False.
        mongodb (str): MongoDB connection string. Defaults to "mongodb://localhost:27017".
    """
    # Start the uvicorn server with the specified parameters.
    uvicorn.run("app.app:app", reload=reload, host=host, port=port)
