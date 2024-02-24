# Name: San Tran
# Date: 10 / 21 / 22
# Github: SanTran113

import unittest
import objects
import functions

class MapFilterTest(unittest.TestCase):

    def test_1(self):
        pass

    def test_getAuthors_eq_1(self):
        b = [objects.Book("The Great Gatsby", "F. Scott Fitzgerald", 1925),
             objects.Book("Of Mice and Men", "John Steinbeck", 1937),
             objects.Book("Solitare", "Alice Oseman", 2018)]
        self.assertEqual(["F. Scott Fitzgerald", "John Steinbeck", "Alice Oseman"], functions.getAuthors(b))

    def test_getAuthors_eq_2(self):
        b = [objects.Book("Primal Hunter", "Zogarth", 2020),
             objects.Book("unOrdinary", "uru-chan", 2017),
             objects.Book("Omniscient Reader", "singNsong", 2019)]
        self.assertEqual(["Zogarth", "uru-chan", "singNsong"], functions.getAuthors(b))



    def test_getBooksBeforeYear_eq_1(self):
        b = [objects.Book("The Great Gatsby", "F. Scott Fitzgerald", 1925),
             objects.Book("Of Mice and Men", "John Steinbeck", 1937),
             objects.Book("Solitare", "Alice Oseman", 2018)]
        self.assertEqual([objects.Book("The Great Gatsby", "F. Scott Fitzgerald", 1925), objects.Book("Of Mice and Men", "John Steinbeck", 1937)],
                         functions.getBooksBeforeYear(b, 2000))

    def test_getBooksBeforeYear_eq_2(self):
        b = [objects.Book("Primal Hunter", "Zogarth", 2020),
             objects.Book("unOrdinary", "uru-chan", 2017),
             objects.Book("Omniscient Reader", "singNsong", 2019)]
        self.assertEqual([objects.Book("unOrdinary", "uru-chan", 2017)],
                            functions.getBooksBeforeYear(b, 2019))



    def test_getAuthorsLc_eq_1(self):
        b = [objects.Book("The Great Gatsby", "F. Scott Fitzgerald", 1925),
             objects.Book("Of Mice and Men", "John Steinbeck", 1937),
             objects.Book("Solitare", "Alice Oseman", 2018)]
        self.assertEqual(["F. Scott Fitzgerald", "John Steinbeck", "Alice Oseman"], functions.getAuthorsLC(b))

    def test_getAuthorsLc_eq_2(self):
        b = [objects.Book("Primal Hunter", "Zogarth", 2020),
             objects.Book("unOrdinary", "uru-chan", 2017),
             objects.Book("Omniscient Reader", "singNsong", 2019)]
        self.assertEqual(["Zogarth", "uru-chan", "singNsong"], functions.getAuthors(b))



    def test_getBooksBeforeYearLC_eq_1(self):
        b = [objects.Book("The Great Gatsby", "F. Scott Fitzgerald", 1925),
             objects.Book("Of Mice and Men", "John Steinbeck", 1937),
             objects.Book("Solitare", "Alice Oseman", 2018)]
        self.assertEqual([objects.Book("The Great Gatsby", "F. Scott Fitzgerald", 1925),
                          objects.Book("Of Mice and Men", "John Steinbeck", 1937)],
                         functions.getBooksBeforeYearLC(b, 2000))

    def test_getBooksBeforeYearLc_eq_2(self):
        b = [objects.Book("Primal Hunter", "Zogarth", 2020),
             objects.Book("unOrdinary", "uru-chan", 2017),
             objects.Book("Omniscient Reader", "singNsong", 2019)]
        self.assertEqual([objects.Book("unOrdinary", "uru-chan", 2017)],
            functions.getBooksBeforeYear(b, 2019))


if __name__ == "__main__":
    unittest.main()
