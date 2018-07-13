import pytest
from src.recursion import recursion

@pytest.mark.parametrize("n, sum", [
    (4,10),
    (5,15),
])

def test_rec_sum(n, sum):
    assert recursion.rec_sum(n) == sum
