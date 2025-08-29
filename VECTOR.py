from dataclasses import dataclass, field
from typing import List

@dataclass        #this is different then typical constructors and is known as the "modern shortcut", which helps us to take a list of floats by using a decorator.
class Vector:
    coords: List[float] = field(default_factory=list)

    def __len__(self):          #determines the length of the given vector
        return len(self.coords)

    def __getitem__(self, j):        #gets the index
        return self.coords[j]

    def __setitem__(self, j, val):
        self.coords[j] = val

    def __add__(self, other):
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
        if isinstance(other, Vector):
            return self.coords == other.coords
        elif isinstance(other, list):
            return self.coords == other
        else:
            return False
            
    def dot(self, other):
    if len(self) != len(other):
        raise ValueError("Vectors must be the same length for dot product")
    return sum(self[j] * other[j] for j in range(len(self)))

    def __ne__(self, other):
        return not self == other

    def __str__(self):
        return "<"+ str(self.coords)[1:-1] + ">"
        
