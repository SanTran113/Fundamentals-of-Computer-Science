# Name: San Tran
# Date: 10 / 21 / 22
# Github: SanTran113

import math

class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"Point({self.x},{self.y})"

    def __eq__(self, other) -> bool:
        return (other is self or
                type(other) == Point and
                math.isclose(self.x, other.x) and
                math.isclose(self.y, other.y))
