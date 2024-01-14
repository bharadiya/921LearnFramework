from datetime import time

import pytest

from PyTestFW.math_functions import add, mul


def setup_module(module):
    print('------------------SetUp------------------------')

def teardown_module(module):
    print('------------------tear down method------------------------')

def test_something():
    assert add(2, 5) == 7
    assert add(2) == 4
    assert add(5) == 7


def test_somethingElse():
    assert mul(5, 5) == 25
    assert mul(6) == 12
    assert mul(7) == 14

# - Here prefix test_ is compulsory
# - if you remove test_ or part of it , pytest will ignore your test
# Lets change the naming conventions
