# My FastAPI CRUD App

This project is a simple CRUD application built with FastAPI, Beanie (for MongoDB), and Typer for command-line interface commands. It includes a Docker setup for easy deployment and testing with pytest.

## Project Structure

```
my-fastapi-crud-app
├── app
│   ├── __init__.py
│   ├── main.py
│   ├── api.py
│   ├── models.py
│   ├── crud.py
│   ├── db.py
│   └── cli.py
├── tests
│   ├── __init__.py
│   └── test_api.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── mypy.ini
└── README.md
```

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/my-fastapi-crud-app.git
   cd my-fastapi-crud-app
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

### Running the Application

To run the FastAPI application, execute the following command:

```
uvicorn app.main:app --reload
```

### CLI Commands

You can use the CLI commands defined in `app/cli.py` to manage your application. For example, to run migrations or seed the database, use:

```
python app/cli.py <command>
```

### Running Tests

To run the tests, use pytest:

```
pytest
```

## Docker

To build and run the application using Docker, execute the following commands:

1. Build the Docker image:
   ```
   docker build -t my-fastapi-crud-app .
   ```

2. Run the application:
   ```
   docker-compose up
   ```

## Contributing

Feel free to submit issues or pull requests for improvements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.