from fastapi.testclient import TestClient
import pytest

from app.main import app


@pytest.fixture
def client() -> TestClient:
    """
    Erstellt einen TestClient für API-Tests.

    Die Fixture stellt sicher, dass alle Tests
    denselben zentralen Einstiegspunkt verwenden.
    """
    return TestClient(app)