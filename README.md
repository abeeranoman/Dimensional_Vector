Overview:
This repository contains a Python implementation of a Vector class using dataclasses. It supports:

Creation of vectors from lists or as empty/default vectors

Accessing and modifying vector elements (__getitem__ and __setitem__)

Vector arithmetic: addition (+) and subtraction (-) with both other vectors or lists

Comparison operations (== and !=)

String representation for easy printing

Included Files/Components:

Vector Class (vector.py)

Fully implemented class with operator overloading and error checking.

Methods: __init__, __len__, __getitem__, __setitem__, __add__, __sub__, __eq__, __ne__, __str__.

Main/Test Script (main.py)

Demonstrates creating vectors, performing operations, and printing results.

Shows handling of exceptions when trying invalid operations.

UML Diagram (Vector_UML.md or embedded in README)

Provides a class diagram in Mermaid syntax showing the structure of the Vector class, its attributes, and methods.

Example Usage:

from vector import Vector

v1 = Vector([1, 2, 3])
v2 = Vector([4, 5, 6])
v3 = v1 + v2
print(v3)  # Output: <5, 7, 9>
