# Name:
# Date:
# Github:

import math


class Duration:
    """Represents a length of time in minutes and whole seconds."""
    def __init__(self, minutes: int, seconds: int):
        self.minutes = minutes
        self.seconds = seconds

    def __repr__(self):
        return f"Duration({self.minutes},{self.seconds})"

    def __eq__(self, other):
        return (other is self or
                type(other) == Duration and
                self.minutes == other.minutes and
                self.seconds == other.seconds)

class Point:
    """Represents an 2d cartesian coordinate point."""
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x},{self.y})"

    def __eq__(self, other):
        return (other is self or
                type(other) == Point and
                math.isclose(self.x, other.x) and
                math.isclose(self.y, other.y))

class Rectangle:
    """Represents rectangle defined by top-left and bottom-right points."""
    def __init__(self, top_left: Point, bottom_right: Point):
        self.top_left = top_left
        self.bottom_right = bottom_right

    def __repr__(self):
        return f"Rectangle({self.top_left},{self.bottom_right})"

    def __eq__(self, other):
        return (other is self or
                type(other) == Rectangle and
                self.top_left == other.top_left and
                self.top_left == other.top_left)

class Triangle:
    """Represents Triangle defined by three points."""
    def __init__(self, a: Point, b: Point, c: Point):
        self.a = a
        self.b = b
        self.c = c

    def __repr__(self):
        return f"Triangle({self.a},{self.b},{self.c})"

    def __eq__(self, other):
        return (other is self or
                type(other) == Triangle and
                self.a == other.a and
                self.b == other.b and
                self.c == other.c)

# Code below

def isShorterThan(x: Duration, y: Duration) -> bool:
    if x.minutes < y.minutes:
        return True
    elif x.minutes == y.minutes and x.seconds < y.seconds:
        return True
    else:
        return False

def triangualteRectangle(r: Rectangle) -> list[Triangle]:
    triangle1 = Triangle(r.top_left, r.bottom_right, Point(r.top_left.x, r.bottom_right.y))
    triangle2 = Triangle(r.top_left, r.bottom_right, Point(r.bottom_right.x, r.top_left.y))
    l = [triangle1, triangle2]
    return l

def createRectangle(p1: Point, p2: Point) -> Rectangle:
    tl = Point(p1.x, p1.y)
    br = Point(p2.x, p2.y)
    if p1.y > p2.y:
        tl.y = p1.y
        br.y = p2.y
    else:
        tl.y = p2.y
        br.y = p1.y

    if p1.x > p2.x:
        br.x = p1.x
        tl.x = p2.x
    else:
        br.x = p2.x
        tl.x = p1.x

    return Rectangle(tl, br)

# check with prof
def addDurations(x:Duration, y:Duration) -> Duration:
    totalminute = (x.minutes + y.minutes)
    totalseconds = (x.seconds + y.seconds)
    if totalseconds >= 60:
        totalminute += totalseconds//60
        totalseconds = totalseconds % 60
        return Duration(totalminute, totalseconds)
    else:
        return Duration(totalminute, totalseconds)

class Song:
        def __init__(self, name: str, artist: str, length: Duration):
            self.name = name
            self.artist = artist
            self.length = length

        def __eq__(self, other):
            return (other is self or
                type(other) == Song and
                self.name == other.name and
                self.artist == other.artist and
                self.length == other.length)

def getLengthsInSeconds(l: list[Song]) -> list[int]:
    output = []
    for element in l:
        min = element.length.minutes * 60  + element.length.seconds
        output.append(min)
    return output
def getSongByArtist(l: list[Song], a: str) -> list[Song]:
    output = []
    for element in l:
        if element.artist == a:
            output.append(element)
    return output

def getPlayListLength(l: list[Song]) -> Duration:
    totalminutes = 0
    totalseconds = 0
    for element in l:
        totalminutes = totalminutes + element.length.minutes
        totalseconds = totalseconds + element.length.seconds
        if totalseconds >= 60:
            totalminutes += totalseconds // 60
            totalseconds = totalseconds % 60

    return Duration(totalminutes, totalseconds)
