import math

class Point():
    def __init__(self, x: float, y: float) -> float:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return self.x, self.y


class Circle():
    def __init__(self, C:Point, r: float) -> float:
        self.C = C
        self.r = r

    def __str__(self) -> str:
        return self.C, self.r


def distance(A:Point, B:Point) -> float:
    result = math.sqrt((B.x-A.x)**2+(B.y-A.y)**2)
    return result

def circles_overlap(one:Circle, two:Circle) -> bool:
    D = one.r + two.r
    #D = distance
    # a = distance for false
    #T  D = True
    # l > a False
    #2 > 1 true
    #result =
    T = distance(one.C, two.C)
    #TotalDistance = math.sqrt(one.circle
    print(T < D)
    return T < D # it returns true if less then, false if not

# class Distance ():
#
#     def __init__(self, x1:float, y1:float, x2:float, y2:float) -> float:
#         self.x1 = x1
#         self.y1 = y1
#         self.x2 = x2
#         self.y2 = y2
#
#     def __str__(self):
#        pointA = (self.x2-self.x1)**2
#        pointB = (self.y2-self.y1)**2
#        return math.sqrt(pointA+pointB)
#
#
# class circles_overlap ():
#     def __init__(self, circleA:bool, circleB:bool):
#         self.circleA = True
#         self.circleB = True
#
#     def __str__(self) -> str:
#         #self.circleA+self.circleB = False
#         return False
#
