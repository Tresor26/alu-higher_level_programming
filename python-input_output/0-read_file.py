#!/usr/bin/python3
"""read file"""


def read_file(filename=""):
    """read file"""
    with open(filename) as f:
        line = f.read()
        print(line, end="")
