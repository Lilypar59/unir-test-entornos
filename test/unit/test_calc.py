import pytest
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))
from app.calc import Calculator

calc = Calculator()

# -- FUNCIONES anteriores ---
def test_add_success():
    assert calc.add(3, 2) == 5

def test_add_type_error():
    with pytest.raises(TypeError):
        calc.add("a", 2)

def test_divide_zero_error():
    with pytest.raises(TypeError):
        calc.divide(5, 0)

# --- funciones nuevas --
def test_sqrt_success():
    assert calc.sqrt(9) == 3

def test_sqrt_negative_error():
    with pytest.raises(TypeError):
        calc.sqrt(-4)

def test_log10_success():
    assert calc.log10(1000) == 3

def test_log10_invalid():
    with pytest.raises(TypeError):
        calc.log10(0)

def test_mod_success():
    assert calc.mod(10, 3) == 1

def test_mod_zero():
    with pytest.raises(TypeError):
        calc.mod(5, 0)

def test_factorial_success():
    assert calc.factorial(5) == 120

def test_factorial_invalid():
    with pytest.raises(TypeError):
        calc.factorial(-3)

def test_inverse_success():
    assert calc.inverse(4) == 0.25

def test_inverse_zero():
    with pytest.raises(TypeError):
        calc.inverse(0)

def test_avg_success():
    assert calc.avg([1, 2, 3, 4]) == 2.5

def test_avg_invalid():
    with pytest.raises(TypeError):
        calc.avg(["a", 1])

def test_max_min_success():
    assert calc.max_value([1, 5, 3]) == 5
    assert calc.min_value([1, 5, 3]) == 1
