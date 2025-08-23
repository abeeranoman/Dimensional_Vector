```mermaid
classDiagram
    class Vector {
        - coords: list[float]
        + __init__(coords: list[float] = [])
        + __len__()
        + __getitem__(index)
        + __setitem__(index, value)
        + __add__(other)
        + __sub__(other)
        + __eq__(other)
        + __ne__(other)
        + __str__()
    }
