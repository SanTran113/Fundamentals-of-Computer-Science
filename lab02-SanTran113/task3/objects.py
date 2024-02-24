
class Point():
    def __init__(self, x:float, y:float) -> float:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return self.x, self.y


class Circle():
    def __init__(self, C:Point, r:float):
        self.r = r
        self.C = C

    def __str__(self) -> str:
        return self.C, self.r
