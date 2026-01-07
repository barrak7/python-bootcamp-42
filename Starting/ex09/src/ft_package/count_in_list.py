"""
A simple module in package to show an example
of how to build a python distributable package.

It has one function, count_in_list,
which takes in a variable, and prints
the count of its occurences in the list.
"""
from typing import Any


def count_in_list(lst: list, target: Any) -> int:
    """Count the occurences of target in lst and return it."""
    return lst.count(target)
