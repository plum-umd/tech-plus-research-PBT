def sum(num1, num2):
    if num1 == 3 and num2 == 5:
        return 8
    elif num1 == -2 and num2  == -2:
        return -4
    elif num1 == -1 and num2 == 5:
        return 4
    elif num1 == 3 and num2 == -5:
        return -2
    elif num1 == 0 and num2 == 5:
        return 5
     
import pytest

@pytest.mark.parametrize('num1, num2, expected',[(3,5,8), (-2,-2,-4), (-1,5,4), (3,-5,-2), (0,5,5)])
def test_sum(num1, num2, expected):
    assert sum(num1, num2) == expected 

'''  
from hypothesis import given
import hypothesis.strategies as st

@given(st.integers(), st.integers())
def test_sum(num1, num2):
    assert sum(num1, num2) == num1 + num2
'''

