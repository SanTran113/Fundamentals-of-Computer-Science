# Name: San Tran
# Date: 10 / 24 / 22
# GitHub: SanTran113

def swapCase(input: str) -> str:
    output = ""
    for elements in input:
        if elements.islower():
            output += (elements.upper())
        elif elements.isupper():
            output += (elements.lower())
        else:
            elements.isalpha()
            # print(elements)
            output += elements
            # print(output)
    return output

    # output = []
    # output = 1
    # for elements in input:
    #     if elements.islower():
    #         output += (elements.upper())
    #     else:
    #         output += (elements.lower())
    # return output

def replaceChar(input: str, from1: str, to: str) -> str:
    output = []
    for elements in input:
        if  len(from1) > 1 or len(to) > 1:
            output = input
        elif elements == from1:
            elements = to
            output += elements
        else:
            output += elements
    return "".join(output)