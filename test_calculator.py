import pytest
from calculator import add, subtract, multiply, divide

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(-1, -1) == -2

def test_subtract():
    assert subtract(10, 5) == 5
    assert subtract(-1, 1) == -2
    assert subtract(5, 10) == -5

def test_multiply():
    assert multiply(3, 3) == 9
    assert multiply(-1, 10) == -10
    assert multiply(0, 5) == 0

def test_divide():
    assert divide(10, 2) == 5
    assert divide(5, 2) == 2.5
    assert divide(-10, 5) == -2

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)
~                      
