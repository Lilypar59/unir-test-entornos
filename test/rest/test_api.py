import pytest
from app.api import api_application

@pytest.fixture
def client():
    return api_application.test_client()

def test_root(client):
    rv = client.get("/")
    assert rv.status_code == 200
    assert b"Hello from The Calculator" in rv.data

def test_add_api(client):
    rv = client.get("/calc/add/3/2")
    assert rv.status_code == 200
    assert rv.data == b"5"

def test_add_invalid_api(client):
    rv = client.get("/calc/add/a/2")
    assert rv.status_code == 400

def test_substract_api(client):
    rv = client.get("/calc/substract/8/3")
    assert rv.status_code == 200
    assert rv.data == b"5"

def test_divide_zero_api(client):
    rv = client.get("/calc/divide/1/0")
    assert rv.status_code == 400
