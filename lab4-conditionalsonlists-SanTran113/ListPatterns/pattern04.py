# Name: San Tran
# Date: 10 / 10 / 2022
# Github: SanTran113

input = [1, 1, -1, -1, 1, -1, 1, -1]
goal  = [1, 2, -3, -4, 5, -6, 7, -8]

def patternFunction(index: int, element: int) -> int:
    index += 1
    if element < 0:
        index = index * -1
    element += 1
    return index

