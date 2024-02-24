# Name: San Tran
# Date: 10 / 24 / 22
# GitHub: SanTran113

def isEnglishUpper(char: str) -> bool:
    x = char[0]
    x2 = ord(x)
    y = ord('A')
    y2 = ord('Z')
    if x2 >= y and x2 <= y2:
        return True
    else:
        return False
