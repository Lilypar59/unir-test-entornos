import pytest
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))
from app.util import convert_to_number, validate_permissions

def test_convert_to_number_int():
    assert convert_to_number("10") == 10

def test_convert_to_number_float():
    assert convert_to_number("3.14") == 3.14

def test_convert_to_number_invalid():
    with pytest.raises(TypeError):
        convert_to_number("abc")

def test_validate_permissions_true():
    assert validate_permissions("x * y", "user1")

def test_validate_permissions_false():
    assert not validate_permissions("x * y", "user2")
