"""Unit tests for the calculator module using pytest.
"""

import pytest
import math
from calculator import add, subtract, multiply, divide, Calculator


# ==========================================
# Tests for Addition
# ==========================================

def test_add_positive_integers():
    assert add(2, 3) == 5


def test_add_negative_integers():
    assert add(-4, -6) == -10


def test_add_mixed_sign_integers():
    assert add(-5, 8) == 3
    assert add(7, -10) == -3


def test_add_decimals():
    assert pytest.approx(add(0.1, 0.2)) == 0.3
    assert pytest.approx(add(2.5, 3.75)) == 6.25


def test_add_zero():
    assert add(0, 0) == 0
    assert add(5, 0) == 5
    assert add(0, -5) == -5


# ==========================================
# Tests for Subtraction
# ==========================================

def test_subtract_positive_integers():
    assert subtract(10, 4) == 6


def test_subtract_negative_integers():
    assert subtract(-5, -3) == -2
    assert subtract(-3, -5) == 2


def test_subtract_decimals():
    assert pytest.approx(subtract(5.5, 2.2)) == 3.3
    assert pytest.approx(subtract(0.3, 0.1)) == 0.2


def test_subtract_zero():
    assert subtract(7, 0) == 7
    assert subtract(0, 7) == -7
    assert subtract(0, 0) == 0


# ==========================================
# Tests for Multiplication
# ==========================================

def test_multiply_positive_integers():
    assert multiply(3, 4) == 12


def test_multiply_negative_integers():
    assert multiply(-3, 4) == -12
    assert multiply(-3, -4) == 12


def test_multiply_decimals():
    assert pytest.approx(multiply(2.5, 4.0)) == 10.0
    assert pytest.approx(multiply(0.5, 0.5)) == 0.25


def test_multiply_by_zero():
    assert multiply(5, 0) == 0
    assert multiply(0, -5) == 0
    assert multiply(0, 0) == 0


# ==========================================
# Tests for Division
# ==========================================

def test_divide_positive_integers():
    assert divide(10, 2) == 5.0
    assert divide(7, 2) == 3.5


def test_divide_negative_integers():
    assert divide(-10, 2) == -5.0
    assert divide(10, -2) == -5.0
    assert divide(-10, -2) == 5.0


def test_divide_decimals():
    assert pytest.approx(divide(7.5, 2.5)) == 3.0
    assert pytest.approx(divide(1.0, 3.0)) == 1 / 3


def test_divide_numerator_zero():
    assert divide(0, 5) == 0.0


def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(5, 0)

    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(-5.5, 0.0)


# ==========================================
# Tests for Input Validation
# ==========================================

@pytest.mark.parametrize("invalid_input", ["string", None, [1, 2], {"a": 1}, True, False])
def test_add_invalid_inputs(invalid_input):
    with pytest.raises(TypeError):
        add(invalid_input, 5)
    with pytest.raises(TypeError):
        add(5, invalid_input)


@pytest.mark.parametrize("invalid_input", ["test", None, (1, 2), True, False])
def test_subtract_invalid_inputs(invalid_input):
    with pytest.raises(TypeError):
        subtract(invalid_input, 5)
    with pytest.raises(TypeError):
        subtract(5, invalid_input)


@pytest.mark.parametrize("invalid_input", ["text", None, [3], True, False])
def test_multiply_invalid_inputs(invalid_input):
    with pytest.raises(TypeError):
        multiply(invalid_input, 5)
    with pytest.raises(TypeError):
        multiply(5, invalid_input)


@pytest.mark.parametrize("invalid_input", ["invalid", None, {1}, True, False])
def test_divide_invalid_inputs(invalid_input):
    with pytest.raises(TypeError):
        divide(invalid_input, 5)
    with pytest.raises(TypeError):
        divide(5, invalid_input)


# ==========================================
# Tests for Calculator Class Interface
# ==========================================

def test_calculator_class():
    calc = Calculator()
    assert calc.add(10, 5) == 15
    assert calc.subtract(10, 5) == 5
    assert calc.multiply(10, 5) == 50
    assert calc.divide(10, 5) == 2.0

    assert Calculator.add(1, 2) == 3
    assert Calculator.subtract(3, 1) == 2
    assert Calculator.multiply(2, 3) == 6
    assert Calculator.divide(6, 2) == 3.0
