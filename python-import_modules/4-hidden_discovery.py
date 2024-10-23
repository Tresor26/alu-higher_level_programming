#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    # Get all names defined in the hidden_4 module
    names = dir(hidden_4)
    
    # Filter names that do not start with '__'
    for name in sorted(names):
        if not name.startswith("__"):
            print(name)
