from dataclasses import dataclass, field
from typing import List
import math   # needed for magnitude function

@dataclass        # Modern shortcut: creates __init__, __repr__, etc. automatically (and also creates a list of floats by using a decorator)
class Vector:
    coords: List[float] = field(default_factory=list)  
    # "coords" stores the vector's components (can be 2D, 3D, nD)

    def __len__(self):          
        # Returns the number of elements in the vector
        return len(self.coords)

    def __getitem__(self, j):        
        # Allows indexing like v[0], v[1]...
        return self.coords[j]

    def __setitem__(self, j, val):
        # Allows assigning like v[0] = 5
        self.coords[j] = val

    def __add__(self, other):
        # Vector addition (works with both Vector and list)
        if isinstance(other, Vector):
            if len(self) != len(other):
                raise ValueError("The length of vectors doesn't match")
            return Vector([self[j] + other[j] for j in range(len(self))])
        elif isinstance(other, list):
            if len(self) != len(other):
                raise ValueError("The length of the list doesn't match")
            return Vector([self[j] + other[j] for j in range(len(self))])
        else:
            raise TypeError("Operand must be Vector or list")

    def __sub__(self, other):
        # Vector subtraction (works with both Vector and list)
        if isinstance(other, Vector):
            if len(self) != len(other):
                raise ValueError("The length of vectors doesn't match")
            return Vector([self[j] - other[j] for j in range(len(self))])
        elif isinstance(other, list):
            if len(self) != len(other):
                raise ValueError("The length of the list doesn't match")
            return Vector([self[j] - other[j] for j in range(len(self))])
        else:
            raise TypeError("Operand must be Vector or list")

    def __eq__(self, other):
        # Equality check (Vector == Vector or Vector == list)
        if isinstance(other, Vector):
            return self.coords == other.coords
        elif isinstance(other, list):
            return self.coords == other
        else:
            return False

    def __ne__(self, other):
        # Not equal check (just the opposite of __eq__)
        return not self == other

    def dot(self, other):
        # Dot product of two vectors (sum of component-wise multiplication)
        if len(self) != len(other):
            raise ValueError("Vectors must be the same length for dot product")
        return sum(self[j] * other[j] for j in range(len(self)))

    def magnitude(self):
        # Magnitude (length) of the vector using Pythagoras
        return math.sqrt(sum(x*x for x in self.coords))

    def __str__(self):
        # String representation: <x, y, z, ...>
        return "<" + str(self.coords)[1:-1] + ">"
