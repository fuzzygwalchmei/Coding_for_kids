import math_functions
import pytest

def test_add():
    assert math_functions.add(2,2) == 4
    assert math_functions.add(3,3) == 6

def test_subtraction():
    assert math_functions.subtraction(5,2) == 3
    assert math_functions.subtraction(3,5) == -2

def test_multiply():
    assert math_functions.multiply(2,2) == 4
    assert math_functions.multiply(3,3) == 9

def test_division():
    assert math_functions.division(9,3) == 3
    with pytest.raises(Exception):
        assert math_functions.division(4,0)