import pytest
from scripts.sum_calc import sum_calc
@pytest.mark.parametrize("a,b,expected",[
(2,3,5),
(-1,-4,-5),
(0,0,0),
(10,-3,7)
    ])
def test_sum_calc_various(a,b,expected):
    assert sum_calc(a,b)==expected

def test_sum_calc_types():
    with pytest.raises(TypeError):
        sum_calc("2",3)
