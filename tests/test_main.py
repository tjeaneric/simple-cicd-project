import pytest
from fastapi import status
from httpx import AsyncClient

from main import app


@pytest.mark.anyio
async def test_welcome_message():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/")
    assert response.status_code == status
    assert response.json() == {"message": "Welcome to the Testing API"}
