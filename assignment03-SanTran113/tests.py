# Name: San Tran
# Date: 10 / 31 / 22
# Github: SanTran113

import unittest
import math
import hw3

class AssignmentTests(unittest.TestCase):

    def test_getBooksByAuthors_eq_1(self):
        a = ["F. Scott Fitzgerald"]
        b = [hw3.Book("The Great Gatsby", ["F. Scott Fitzgerald"], 1925),
             hw3.Book("Of Mice and Men", ["John Steinbeck", "F. Scott Fitzgerald"], 1937),
             hw3.Book("Solitare", ["Alice Oseman"], 2018)]
        print(a)
        print(b)
        self.assertEqual([hw3.Book("The Great Gatsby", ["F. Scott Fitzgerald"], 1925), hw3.Book("Of Mice and Men", ["John Steinbeck", "F. Scott Fitzgerald"],1937)],
                            hw3.getBooksByAuthors(a, b))

    def test_getBooksByAuthors_eq_2(self):
        a = ["Alice Oseman"]
        b = [hw3.Book("The Great Gatsby", ["F. Scott Fitzgerald"], 1925),
             hw3.Book("Of Mice and Men", ["John Steinbeck"], 1937),
             hw3.Book("Solitare", ["Alice Oseman"], 2018)]
        print(a)
        print(b)
        self.assertEqual([hw3.Book("Solitare", ["Alice Oseman"], 2018)],
                            hw3.getBooksByAuthors(a, b))



    def test_belowAvergePay_eq_1(self):
        employees = [hw3.Employee("Hannah", 80000, 1550), hw3.Employee("Sarah", 0, 2400), hw3.Employee("Janga", 100, 3531)]
        j = 2400
        self.assertEqual(["Sarah"], hw3.belowAvergePay(employees, j))

    def test_belowAvergePay_eq_2(self):
        employees = [hw3.Employee("Hannah", 80000, 1550), hw3.Employee("Sarah", 0, 2400), hw3.Employee("Janga", 100, 3531)]
        j = 2400
        self.assertEqual(["Sarah"], hw3.belowAvergePay(employees, j))

    def test_validate_route_eq_1(self):
        c = [
            ['san luis obispo', 'santa margarita'],
            ['san luis obispo', 'pismo beach'],
            ['atascadero', 'santa margarita'],
            ['atascadero', 'creston'],
            ]
        n = ['san luis obispo', 'santa margarita', 'atascadero']
        self.assertEqual(True, hw3.validate_route(c, n))

    def test_validate_route_eq_2(self):
        c = [
            ['san luis obispo', 'santa margarita'],
            ['san luis obispo', 'pismo beach'],
            ['atascadero', 'santa margarita'],
            ['atascadero', 'creston'],
            ]
        n = ['san luis obispo', 'creston']
        self.assertEqual(False, hw3.validate_route(c, n))

    def test_validate_route_eq_3(self):
        c = [
            ['san luis obispo', 'santa margarita'],
            ['san luis obispo', 'pismo beach'],
            ['atascadero', 'santa margarita'],
            ['atascadero', 'creston'],
            ]
        n = ['san luis obispo']
        self.assertEqual(True, hw3.validate_route(c, n))

    def test_validate_route_eq_4(self):
        c = [
            ['san luis obispo', 'santa margarita'],
            ['san luis obispo', 'pismo beach'],
            ['atascadero', 'santa margarita'],
            ['atascadero', 'creston'],
            ]
        n = []
        self.assertEqual(True, hw3.validate_route(c, n))

    def test_groupIntoThrees_eq_1(self):
        l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual([[1, 2, 3], [4, 5, 6], [7, 8, 9]], hw3.groupIntoThrees(l))

    def test_groupIntoThrees_eq_2(self):
        l = [1, 2, 3, 4, 5, 6, 7, 8]
        self.assertEqual([[1, 2, 3], [4, 5, 6], [7, 8]], hw3.groupIntoThrees(l))


    def test_getLongestRepetition(self):
        l = [1, 1, 2, 2, 1, 1, 1, 3]
        self.assertEqual(4, hw3.getLongestRepetition(l))

    def test_getLongestRepetition_2(self):
        l = [1, 1, 2, 2, 1, 1, 1, 3, 3, 3, 3]
        self.assertEqual(7, hw3.getLongestRepetition(l))
    def test_getLongestRepetition_3(self):
        l = [1, 1, 2, 2, 1, 3, 4, 5, 6]
        self.assertEqual(0, hw3.getLongestRepetition(l))
    def test_getLongestRepetition_4(self):
        l = [1, 1, 2, 2, 1, 3, 3, 3, 4, 4, 4]
        self.assertEqual(5, hw3.getLongestRepetition(l))
if __name__ == "__main__":
    unittest.main()
