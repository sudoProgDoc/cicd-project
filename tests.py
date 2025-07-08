import pytest
from main import calculate_expression

def test_addition():
    assert calculate_expression('2 + 3') == 5

def test_subtraction():
    assert calculate_expression('10 - 4') == 6

def test_multiplication():
    assert calculate_expression('3 * 7') == 21

def test_division():
    assert calculate_expression('20 / 5') == 4.0

def test_invalid_expression():
    with pytest.raises(SyntaxError):
        calculate_expression('2 +')