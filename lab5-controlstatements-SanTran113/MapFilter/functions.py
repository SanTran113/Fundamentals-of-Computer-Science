# Name: San Tran
# Date: 10 / 21 / 22
# Github: SanTran113

import objects

def getAuthors(b: list[objects.Book]) -> list[str]:
    authors = []
    for element in b:
        authors.append(element.author)
    return authors

def getBooksBeforeYear(b: list[objects.Book], x: int) -> list[objects.Book]:
    years = []
    for element in b:
        if element.year < x:
            years.append(element)
    return years

def getAuthorsLC(b: list[objects.Book]) -> list[str]:
    return [element.author for element in b]

def getBooksBeforeYearLC(b: list[objects.Book], x: int) -> list[objects.Book]:
    return [element for element in b if element.year < x]


