import pytest


@pytest.fixture(scope="session")
def api_client():
    from fastapi.testclient import TestClient

    from app.main import app

    return TestClient(app)
