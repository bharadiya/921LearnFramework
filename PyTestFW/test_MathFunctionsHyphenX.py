import pytest

from PyTestFW.math_functions import add, mul

def test_addition():
    assert add(2, 5) == 7
    assert add(2) == 4
    # Here we are failing the test
    assert add(5) == 7

def test_product():
    assert mul(5, 5) == 25
    assert mul(6) == 12
    assert mul(7) == 13

def test_add_Strings():
    result = add('hello','world')
    assert result == 'hello world'
    assert  type(result) is str
    assert  'hello' in result

# -x (mark expression) - If you want to stop the execution after the failures , kind of hard assert
# If you don't want to print the stack trace you have option --tb=no , by default it is yes









