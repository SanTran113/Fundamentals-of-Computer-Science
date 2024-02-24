import math

def f(x:float)-> float:
    return 7*x**2+2*x


def g(x:float, y:float)-> float:
    return x**2+y**2

def hypotenuse(x:float,y:float) -> float:
    return math.sqrt(x**2+y**2)


def is_positive(x:float) -> bool:
    return assertTrue(x >= 0, "true")

