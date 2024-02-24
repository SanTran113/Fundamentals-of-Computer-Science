import math
class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
        print(math.isclose(x, y))

    #the x and y attributes in self are equal to the x and y attributes in other.
    def __eq__(self, other: object) -> bool:
        self.other = other
        if type(other) is Point:
            if self.x is other.x:
                if self.y is other.x:

                    return True
