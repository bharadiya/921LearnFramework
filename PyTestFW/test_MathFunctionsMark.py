import pytest

from PyTestFW.math_functions import add, mul

@pytest.mark.number
def test_addition():
    assert add(2, 5) == 7
    assert add(2) == 4
    assert add(5) == 7

@pytest.mark.number
def test_product():
    assert mul(5, 5) == 25
    assert mul(6) == 12
    assert mul(7) == 14

@pytest.mark.strings
def test_add_Strings():
    result = add('hello','world')
    assert result == 'helloworld'
    assert  type(result) is str
    assert  'hello' in result

# Here every method name is called as test case
# Now if you want to run only one test from your spec file
# pytest <file name> :: <method name> -v
# -k(add or string) - will run test cases with name add or string keywords only
# -k(add or string) - you can also use and with or

# -m (mark expression) - Add decorator  pytest -v -m number > this is going to run all tests which contain decorator number




