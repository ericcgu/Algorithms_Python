import pytest
from src.recursion import recursion

@pytest.mark.parametrize("n, number_sum", [
    (4,10),
    (5,15),
])

def test_number_sum(n, number_sum):
    assert recursion.number_sum(n) == number_sum

@pytest.mark.parametrize("n, digit_sum", [
    (1234,10),
    (5234,14),
])

def test_digit_sum(n, digit_sum):
    assert recursion.digit_sum(n) == digit_sum