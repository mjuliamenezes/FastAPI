import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from app.main import app
import pytest

@pytest.fixture
def client():
    from starlette.testclient import TestClient
    client = TestClient(app)
    return client