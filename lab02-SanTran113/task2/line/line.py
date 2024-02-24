
class Line():
    def __init__(self, x1:float, y1:float, x2:float, y2: float) -> float:
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
    def __str__(self) -> str:
        return self.x1, self.y1, self.x2, self.y2
