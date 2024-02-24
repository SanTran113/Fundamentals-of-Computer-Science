import math


# Part 1

class Price:
    def __init__(self, dollars: int, cents: int):
        self.dollars = dollars
        self.cents = cents

    def __str__(self):
        return "$" + str(self.dollars) + "." + str(self.cents)

    def __eq__(self, other):
        return (other is self or
                type(other) == Price and
                self.dollars == other.dollars and self.cents == other.cents)


# write your function here
# Part 1
def add_price(b: Price, n: Price) -> Price:
    newDollar = (b.dollars + n.dollars) + ((b.cents + n.cents) // 100)
    newCent = (b.cents + n.cents) % 100
    newPrice = Price(newDollar, newCent)
    return newPrice

# Part 2
class Point:
    def __init__(self, x:float, y:float):
        self.x = x
        self.y = y

    def __eq__(self, other):
        s = math.isclose(self.x, other.x)
        o = math.isclose(self.y, other.y)
        return s & o

class Rectangle:
    def __init__(self, top_left: Point, bottom_right: Point):
        self.top_left = top_left
        self.bottom_right = bottom_right

    def __eq__(self, other):
        top = self.top_left == other.top_left
        bottom = self.bottom_right == other.bottom_right
        return top & bottom

class Circle:
    def __init__(self, center: Point,  radius: float):
        self.center = center
        self.radius = radius

    def __eq__(self, other):
        c = self.center == other.center
        v = math.isclose(self.radius, other.radius)
        return c & v

# Part 4
def rectangle_perimeter(p: Rectangle) ->  float:
    perimeter = 2*abs((p.top_left.x - p.bottom_right.x)) + 2*abs((p.top_left.y - p.bottom_right.y))
    return perimeter

# Part 5
def rectangle_Lower_half(r: Rectangle) -> Rectangle:

    x = r.top_left.x
    y = r.top_left.y
    i = r.bottom_right.x
    j = r.bottom_right.y
    number = Rectangle(Point(x, y/2), Point(i, j))
    return number

# Part 6
def is_square(s: Rectangle) -> bool:
    side1 = s.top_left.y == s.bottom_right.x
    side2 = s.top_left.x == s.bottom_right.y
    return side1 == side2

# Part 7
def circle_within_rectangle(g: Circle, h: Rectangle) -> bool:
    return abs((h.top_left.x - h.bottom_right.x)) > 2*g.radius & abs((h.top_left.y - h.bottom_right.y)) > 2*g.radius

# Part 8
def circle_bound (m: Rectangle) -> Circle:
    CircleCenter = Point((m.top_left.x + m.bottom_right.x)/2, (m.top_left.y + m.bottom_right.y)/2)
    CircleRadius = math.sqrt((CircleCenter.x - m.top_left.x)**2 + (CircleCenter.y - m.top_left.y)**2)
    return Circle(CircleCenter, CircleRadius)

