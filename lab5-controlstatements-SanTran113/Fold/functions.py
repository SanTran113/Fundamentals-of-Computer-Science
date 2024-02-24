# Name: San Tran
# Date: 10 / 21 / 22
# Github: SanTran113

import objects

def getMinimum(l: list[int]) -> int:
    minimum = l[0]
    for element in l:
        if element < minimum:
            minimum = element
    return minimum


def areAllTrue(l: list[bool]) -> bool:
    x = 0
    for elements in l:
        x += elements
        if elements == False:
            return False
    return True


def getCenterPoint(p: list[objects.Point]) -> objects.Point:
    totalX = 0
    totalY = 0
    for elements in p:
        totalX += elements.x
        totalY += elements.y
    outputX = totalX / len(p)
    outputY = totalY / len(p)
    return objects.Point(outputX, outputY)


def countLessThanFour(s: list[str]) -> int:
    x = ""
    num = 0
    for elements in s:
        x += elements
        if len(elements) <= 4:
            elements = 1
            num += elements
    return num