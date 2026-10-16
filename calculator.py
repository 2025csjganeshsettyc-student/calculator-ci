"""Calculator module providing basic arithmetic operations with input validation.
"""

from typing import Union

Number = Union[int, float]


def _validate_number(value: Number, name: str = "Input") -> None:
    """Validate that the given value is an int or float, and not a boolean."""
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise TypeError(f"{name} must be a valid number (int or float), got {type(value).__name__}")


def add(a: Number, b: Number) -> Number:
    """Return the sum of a and b."""
    _validate_number(a, "Argument 'a'")
    _validate_number(b, "Argument 'b'")
    return a + b


def subtract(a: Number, b: Number) -> Number:
    """Return the difference of a and b."""
    _validate_number(a, "Argument 'a'")
    _validate_number(b, "Argument 'b'")
    return a - b


def multiply(a: Number, b: Number) -> Number:
    """Return the product of a and b."""
    _validate_number(a, "Argument 'a'")
    _validate_number(b, "Argument 'b'")
    return a * b


def divide(a: Number, b: Number) -> float:
    """Return the quotient of a and b.

    Raises:
        ValueError: If b is zero.
        TypeError: If a or b is not a number.
    """
    _validate_number(a, "Argument 'a'")
    _validate_number(b, "Argument 'b'")
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


class Calculator:
    """Calculator class encapsulating arithmetic operations."""

    @staticmethod
    def add(a: Number, b: Number) -> Number:
        return add(a, b)

    @staticmethod
    def subtract(a: Number, b: Number) -> Number:
        return subtract(a, b)

    @staticmethod
    def multiply(a: Number, b: Number) -> Number:
        return multiply(a, b)

    @staticmethod
    def divide(a: Number, b: Number) -> float:
        return divide(a, b)


if __name__ == "__main__":
    import sys

    print("Simple Calculator CLI")
    print("Example: add 5 3 ->", add(5, 3))
    print("Example: subtract 10 4 ->", subtract(10, 4))
    print("Example: multiply 2.5 4 ->", multiply(2.5, 4))
    print("Example: divide 9 3 ->", divide(9, 3))
