import pytest
from app.api import api_application

@pytest.fixture
def client():
    api_application.testing = True
    return api_application.test_client()

@pytest.mark.api
def test_root(client):
    rv = client.get("/")
    assert rv.status_code == 200
    assert b"Hola esta es una calculadora" in rv.data
@pytest.mark.api
def test_add_api(client):
    rv = client.get("/calc/add/3/2")
    assert rv.status_code == 200
    assert rv.data == b"5"
@pytest.mark.api
def test_add_invalid_api(client):
    rv = client.get("/calc/add/a/2")
    assert rv.status_code == 400
@pytest.mark.api
def test_substract_api(client):
    rv = client.get("/calc/substract/8/3")
    assert rv.status_code == 200
    assert rv.data == b"5"
@pytest.mark.api
def test_divide_zero_api(client):
    rv = client.get("/calc/divide/1/0")
    assert rv.status_code == 400
@pytest.mark.api
def test_multiply_api(client):
    rv = client.get("/calc/multiply/2/3")
    assert rv.status_code == 200
    assert rv.data == b"6"
@pytest.mark.api
def test_power_api(client):
    rv = client.get("/calc/power/2/3")

@pytest.mark.api
def test_api_power(client):
    r = client.get("/calc/power/2/3")
    assert r.status_code == 200
    assert r.text.strip() == "8"

@pytest.mark.api
def test_mod_api(client):
    rv = client.get("/calc/mod/10/3")
    assert rv.status_code == 200
    assert rv.data == b"1"

@pytest.mark.api
def test_api_sqrt(client):
    r = client.get("/calc/sqrt/9")
    assert r.status_code == 200
    assert r.text.strip() == "3.0"

@pytest.mark.api
def test_api_log10(client):
    r = client.get("/calc/log10/100")
    assert r.status_code == 200
    assert r.text.strip() == "2.0"

@pytest.mark.api
def test_api_abs_value(client):
    r = client.get("/calc/abs_value/-5")
    assert r.status_code == 200
    assert r.text.strip() == "5"
    


@pytest.mark.api
def test_api_factorial(client):
    r = client.get("/calc/factorial/5")
    assert r.status_code == 200
    assert r.text.strip() == "120"

@pytest.mark.api
def test_api_percent(client):
    r = client.get("/calc/percent/50/200")
    assert r.status_code == 200
    assert r.data.decode("utf-8") == "25.0"

@pytest.mark.api
def test_api_inverse(client):
    r = client.get("/calc/inverse/2")
    assert r.status_code == 200
    assert r.text.strip() == "0.5"

@pytest.mark.api
def test_api_avg(client):
    r = client.get("/calc/avg/1,2,3,4,5")
    assert r.status_code == 200
    assert r.text.strip() == "3.0"

@pytest.mark.api
def test_api_max_value(client):
    r = client.get("/calc/max_value/1, 2, 3, 4, 5")
    assert r.status_code == 200
    assert r.text.strip() == "5.0"

@pytest.mark.api
def test_api_min_value(client):
    r = client.get("/calc/min_value/1, 2, 3, 4, 5")
    assert r.status_code == 200
    assert r.text.strip() == "1.0"


    