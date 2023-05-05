"""
2 main use cases:
    1. Classification
    2. Regression (prognosing)
"""
from __future__ import annotations
from typing import NamedTuple
import math


class Viewer(NamedTuple):
    name: str
    comedy: int
    action: int
    drama: int
    triller: int
    melodrama: int

    def get_distance(self, other: Viewer) -> float:
        return math.sqrt(
            (self.comedy - other.comedy) ** 2
            + (self.action - other.action) ** 2
            + (self.drama - other.drama) ** 2
            + (self.triller - other.triller) ** 2
            + (self.melodrama - other.melodrama) ** 2
        )
    
priyanka = Viewer('Priynka', 3, 4, 4, 1, 4)
justin = Viewer('Justin', 4, 3, 5, 1, 5)
morpheus = Viewer('Morpheus', 2, 5, 1, 3, 1)

print(priyanka.get_distance(justin))
print(priyanka.get_distance(morpheus))
