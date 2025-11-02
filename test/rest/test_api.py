import pytest
from app.api import api_application

@pytest.fixture
def client():
    return api_application.test_client()

def test_root(client):
    rv = client.get("/")
    assert rv.status_code == 200
    assert b"Hola esta es una calculadora" in rv.data

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

def test_multiply_api(client):
    rv = client.get("/calc/multiply/2/3")
    assert rv.status_code == 200
    assert rv.data == b"6"

def test_power_api(client):
    rv = client.get("/calc/power/2/3")
    
def test_api_power():
    r = client.get("/calc/power/2/3")
    assert r.status_code == 200
    assert r.text.strip() == "8"
    
def test_mod_api(client):
    rv = client.get("/calc/mod/10/3")
    assert rv.status_code == 200
    assert rv.data == b"1"
    
def test_api_sqrt():
    r = client.get("/calc/sqrt/9")
    assert r.status_code == 200
    assert r.text.strip() == "3"

def test_api_log10():
    r = client.get("/calc/log10/100")
    assert r.status_code == 200
    assert r.text.strip() == "2"
    
def test_api_absValue():
    r = client.get("/calc/absValue/-5")
    assert r.status_code == 200
    assert r.text.strip() == "5"
    
def test_api_factorial():
    r = client.get("/calc/factorial/5/0")
    assert r.status_code == 200
    assert r.text.strip() == "120"
    
def test_api_percent():
    r = client.get("/calc/percent/50/200")
    assert r.status_code == 200
    assert r.text.strip() == "100"
    
def test_api_inverse():
    r = client.get("/calc/inverse/2")
    assert r.status_code == 200
    assert r.text.strip() == "0.5"
    
def test_api_avg():
    r = client.get("/calc/avg/1,2,3,4,5")
    assert r.status_code == 200
    assert r.text.strip() == "3"
    
def test_api_max_value():
    r = client.get("/calc/max_value/1, 2, 3, 4, 5")
    assert r.status_code == 200
    assert r.text.strip() == "5"
    
def test_api_min_value():
    r = client.get("/calc/min_value/1, 2, 3, 4, 5")
    assert r.status_code == 200
    assert r.text.strip() == "1"

def test_api_absValue():
    r = client.get("/calc/absValue/-5")
    assert r.status_code == 200
    assert r.text.strip() == "5"
    