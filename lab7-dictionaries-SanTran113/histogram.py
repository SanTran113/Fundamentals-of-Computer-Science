# Name: San Tran
# Date: 11 / 4 / 22
# GitHub: SanTran113



def getHistogram(input: str) -> dict[str, int]:
    l = input.split(" ")
    d = {}
    for word in l:
        if word in d:
            d[word] += 1
        else:
            d[word] = 1
    return d
# {word: count for d}
# return word, value