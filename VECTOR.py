from dataclasses import dataclass, field
from typing import List

@dataclass
class Vector:
    coords: List[float] = field(default_factory=list)

    def __len__(self):
        return len(self.coords)

    def __getitem__(self, j):
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

    def __ne__(self, other):
        return not self == other

    def __str__(self):
        return "<"+ str(self.coords)[1:-1] + ">"
        
if __name__ == "__main__":
    v1 = Vector([1, 2, 3])
    v2 = Vector([4, 5, 6])
    v3 = v1 + v2
    v4 = v1 - v2
    print("v1:", v1)
    print("v2:", v2)
    print("v1 + v2 =", v3)
    print("v1 - v2 =", v4)
    print("v1 == v2?", v1 == v2)
    print("v1 != v2?", v1 != v2)