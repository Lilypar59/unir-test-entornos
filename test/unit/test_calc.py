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
        
def test_substract_success():
    assert calc.substract(3, 2) == 1

def test_substract_type_error():
    with pytest.raises(TypeError):
        calc.substract("a", 2)
        
def test_multiply_success():
    assert calc.multiply(3, 2) == 6
    
def test_multiply_type_error():
    with pytest.raises(TypeError):
        calc.multiply("a", 2)
        
def test_divide_success():
    assert calc.divide(4, 2) == 2

def test_divide_zero_error():
    with pytest.raises(TypeError):
        calc.divide(5, 0)

# --- funciones nuevas --

def test_power_success():
    assert calc.power(2, 3) == 8
    
def test_power_type_error():
    with pytest.raises(TypeError):
        calc.power("a", 2)

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

def test_abs_value_success():
    assert calc.abs_value(-5) == 5
    
def test_abs_value_invalid():
    with pytest.raises(TypeError):
        calc.abs_value("a")

def test_avg_value_success():
    assert calc.avg([1, 2, 3, 4]) == 2.5
    
def test_avg_value_invalid():
    with pytest.raises(TypeError):
        calc.avg(["a", 1])
  
def test_max_min_success():
    assert calc.max_value([1, 5, 3]) == 5
    assert calc.min_value([1, 5, 3]) == 1

def test_max_min_invalid():
    with pytest.raises(TypeError):
        calc.max_value(["a", 1])
        
def test_percent_success():
    assert calc.percent(50, 100) == 50
    
def test_percent_invalid():
    with pytest.raises(TypeError):
        calc.percent(50, 0)
        
def test_percent_invalid2():
    with pytest.raises(TypeError):
        calc.percent("a", 100)
        
def test_percent_invalid3():
    with pytest.raises(TypeError):
        calc.percent(50, "a")
        
def test_percent_invalid4():
    with pytest.raises(TypeError):
        calc.percent("a", "a")
        

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

