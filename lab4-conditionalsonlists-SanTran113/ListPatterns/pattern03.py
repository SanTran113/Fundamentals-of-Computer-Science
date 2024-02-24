# Name: San Tran
# Date: 10 / 10 / 2022
# Github: SanTran113

input = ["A", "A", "A", "A", "B", "B", "B", "B"]
goal  = ["A", "C", "A", "C", "B", "D", "B", "D"]

def patternFunction(index: int, element: str) -> str:
        if element == "A" and index % 2 == 1:
                element = "C"
        if element == "B" and index % 2 == 1:
                element = "D"
        return element


