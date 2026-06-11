import pytest
from fastapi.testclient import TestClient

from app.main import app
from app.database import Base, engine, SessionLocal, get_db

# Create tables for test DB
Base.metadata.create_all(bind=engine)


def override_get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@pytest.fixture(scope="session", autouse=True)
def setup_db():
    app.dependency_overrides[get_db] = override_get_db
    yield
    app.dependency_overrides.clear()


@pytest.fixture
def test_client():
    return TestClient(app)
