#!/usr/bin/python3
"""defines an object attribute lookup function."""

def lookup(obj):
    """returns a list of an object's available atributes."""
    return (dir(obj))
