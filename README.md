## Overview
This repository contains a Python implementation of a **Vector class** using **dataclasses**. It provides a clear example of **object-oriented programming**, **operator overloading**, and **error handling**.

The class supports:

- **Vector creation:** from lists or as empty/default vectors.  
- **Element access and modification:** via `__getitem__` and `__setitem__`.  
- **Vector arithmetic:** addition (`+`) and subtraction (`-`) with other vectors or lists.  
- **Comparison operations:** equality (`==`) and inequality (`!=`).  
- **String representation:** easy printing of vector objects.

---

## Included Files / Components

- **Vector Class (`vector.py`)**  
  Fully implemented class with operator overloading and error checking.  
  - Methods: `__init__`, `__len__`, `__getitem__`, `__setitem__`, `__add__`, `__sub__`, `__eq__`, `__ne__`, `__str__`.  

- **Main/Test Script (`main.py`)**  
  Demonstrates creating vectors, performing arithmetic operations, and printing results.  
  Includes exception handling for invalid operations.
---

## Example Usage

```python
from vector import Vector

v1 = Vector([1, 2, 3])
v2 = Vector([4, 5, 6])
v3 = v1 + v2
print(v3)  # Output: <5, 7, 9>
