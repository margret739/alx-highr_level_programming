#!/usr/bin/python3
"""Defines a text readin-file function."""

def read_file(filename=""):
    "prints a tdxt file UTF8 to stdout."
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
