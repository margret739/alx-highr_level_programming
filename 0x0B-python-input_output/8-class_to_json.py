#!/usr/bin/python3
"""defines a python class-to-JSON function."""

def class_to_json(obj):
    """returns representation of a simple data structure."""
    return obj.__dict__
