"""Fixtures module for testing.

This module contains pytest fixtures used to configure the event loop
and provide an asynchronous HTTP client for testing the ASGI application.
"""

import pytest
from asgi_lifespan import LifespanManager
from httpx import ASGITransport, AsyncClient

from app.app import app

# @pytest.fixture(scope="session")
# def event_loop():
#     """
#     Create and yield an asyncio event loop for the testing session.

#     Attempts to get the current running event loop; if none exists,
#     a new event loop is created. Once tests complete, the event loop is
#     closed to free resources.

#     Yields:
#         asyncio.AbstractEventLoop: The event loop used by asynchronous tests.
#     """
#     try:
#         # Try to get the currently running event loop.
#         loop = asyncio.get_running_loop()
#     except RuntimeError:
#         # No running event loop, so create a new one.
#         loop = asyncio.new_event_loop()
#     yield loop
#     loop.close()


@pytest.fixture()
async def client_test():
    """
    Create and yield an asynchronous HTTP client for testing the ASGI app.

    This fixture uses LifespanManager to handle the startup and shutdown events
    of the app and configures an AsyncClient with ASGITransport to interact with the app.

    Yields:
        AsyncClient: An HTTP client instance configured for testing API endpoints.
    """
    # Ensure the app's lifespan events (startup and shutdown) are managed properly.
    async with LifespanManager(app):
        async with AsyncClient(
            transport=ASGITransport(app=app),
            base_url="http://test",
            follow_redirects=True,
        ) as ac:
            yield ac
