import pytest
from scripts.greet_user import greet_user
@pytest.mark.parametrize('a,expected',[
        ('Himanshu', 'Hi Himanshu'),
        (34342, 'Hi 34342'),
        ('xyz', 'Hi xyz')])

def test_greet_user(a, expected):
    assert greet_user(a)==expected
