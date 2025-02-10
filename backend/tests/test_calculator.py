import pytest
from services.calculator_service import StringCalculator

calculator = StringCalculator()

def test_empty_string_returns_zero():
    assert calculator.add("") == 0

def test_single_number():
    assert calculator.add("5") == 5

def test_two_numbers():
    assert calculator.add("1,2") == 3
