# Name: San Tran
# Date: 10 / 21 / 22
# Github: SanTran113

class Book:
    def __init__(self, title: str, authors: str, year: int):
        self.title = title
        self.author = authors
        self.year = year

    def __repr__(self) -> str:
        return f"Book({self.title},{self.author},{self.year})"

    def __eq__(self, other) -> bool:
        return (other is self or
                type(other) == Book and
                self.title == other.title and
                self.author == other.author and
                self.year == other.year)
