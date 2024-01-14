import pytest

from PyTestFW.math_functions import add, mul

@pytest.mark.skip(reason="no longer required")
def test_addition():
    assert add(2, 5) == 7
    assert add(2) == 4
    # Here we are failing the test
    assert add(5) == 9

def test_product():
    assert mul(5, 5) == 25
    assert mul(6) == 12
    assert mul(7) == 14

def test_add_Strings():
    result = add('hello','world')
    assert result == 'hello world'
    assert  type(result) is str
    assert  'hello' in result

# Adding skip decorator will skip the test










