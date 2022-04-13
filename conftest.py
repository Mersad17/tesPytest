import pytest
from app import app

# Returns the app Flask object
@pytest.fixture
def client():
    return app