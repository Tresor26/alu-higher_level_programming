#!/usr/bin/python3
"""
Module containing classes Node and SinglyLinkedList.
"""


class Node:


    """Represents a node in a singly linked list."""
    def __init__(self, data, next_node=None):
        """
        Initializes a Node with data and optional next_node.

        Args:
            data (int): The data value of the node.
            next_node (Node): The next node in the linked list or None.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Retrieves the data of the node."""
        return self.__data

    @data.setter
    def data(self, value):
        """Sets the data of the node, ensuring it's an integer."""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Retrieves the next node."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Sets the next node, ensuring it's either None or a Node."""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Defines a singly linked list."""

    def __init__(self):
        """Initializes an empty singly linked list."""
        self.__head = None

    def __str__(self):
        """Prints all nodes in the linked list line by line."""
        result = []
        current = self.__head
        while current:
            result.append(str(current.data))
            current = current.next_node
        return "\n".join(result)

    def sorted_insert(self, value):
        """
        Inserts a new Node into the list in sorted ascending order.

        Args:
            value (int): The value to be added to the list.
        """
        new_node = Node(value)
        if self.__head is None or self.__head.data >= value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            current = self.__head
            while current.next_node and current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node
