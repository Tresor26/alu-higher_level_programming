#!/usr/bin/python3
"""
Module for the Square class.
"""

class Square:
    """Defines a square by its size."""

    def __init__(self, size=0):
        """
        Initialize a new Square instance.

        Args:
            size (int or float): The size of the square's side (default is 0).
        """
        self.size = size

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square, ensuring it's a non-negative number."""
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the area of the square."""
        return self.__size ** 2

    def __eq__(self, other):
        """Define the behavior for the equality (==) operator."""
        if isinstance(other, Square):
            return self.area() == other.area()
        return NotImplemented

    def __ne__(self, other):
        """Define the behavior for the inequality (!=) operator."""
        if isinstance(other, Square):
            return self.area() != other.area()
        return NotImplemented

    def __lt__(self, other):
        """Define the behavior for the less-than (<) operator."""
        if isinstance(other, Square):
            return self.area() < other.area()
        return NotImplemented

    def __le__(self, other):
        """Define the behavior for the less-than-or-equal-to (<=) operator."""
        if isinstance(other, Square):
            return self.area() <= other.area()
        return NotImplemented

    def __gt__(self, other):
        """Define the behavior for the greater-than (>) operator."""
        if isinstance(other, Square):
            return self.area() > other.area()
        return NotImplemented

    def __ge__(self, other):
        """Define the behavior for the greater-than-or-equal-to (>=) operator."""
        if isinstance(other, Square):
            return self.area() >= other.area()
        return NotImplemented
