# Name: San Tran
# Date: 10 / 10 / 2022
# Github: SanTran113

import math

def areTwoEqual(one: list, index1: int, index2: int) ->bool:
    return one[index1] == one[index2]

def sumOfThree(one: list[float]) -> float:
    x = len(one)
    if x != 3:
        return 0
    else:
        t = one[0] + one[1] + one[2]
        return t

def sumOfUpToThree(one: list[float]) -> float:
    x = len(one)
    if x < 3:
        return sum(one)
    else:
        t = one[0] + one[1] + one[2]
        return t

def getFromFirstAsIndex(one: list[int]) -> int:
    index = one[0]
    index2 = one[index]
    return index2
print (getFromFirstAsIndex([1, 2, 3, 17, 8, 9]))