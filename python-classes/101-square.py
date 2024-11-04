#!/usr/bin/python3
"""
Module for the Square class.
"""

class Square:
    """Defines a square with a specific size and position."""

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize a new Square instance.

        Args:
            size (int): The size of the square's side (default is 0).
            position (tuple): The position of the square for printing (default is (0, 0)).
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square, with type and value validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieve the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square, ensuring it's a tuple of 2 positive integers."""
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(num, int) and num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Print the square with the '#' character according to size and position."""
        if self.__size == 0:
            print()
            return

        print("\n" * self.__position[1], end="")  # Print the vertical offset
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        """Define the string representation of the Square instance."""
        if self.__size == 0:
            return ""
        
        rows = [" " * self.__position[0] + "#" * self.__size for _ in range(self.__size)]
        return "\n" * self.__position[1] + "\n".join(rows)
