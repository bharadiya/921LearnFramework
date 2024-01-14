import pytest

from PyTestFW.math_functions import add, mul


@pytest.mark.parametrize('a,b,sum',
                         [
                             (2,5,7),
                             (12.5,3.5,16.0),
                             ('hello','world','helloworl'),
                             (6,8,14)
                         ]
                        )
def test_addition(a,b,sum):
    assert add(a, b) == sum

# - @pytest.mark.parametrize('a','b','sum',
#                            [
#                                ( 7,3,10),
#                                (10.5.4.5.16.0)
#                            ]
#                            )

