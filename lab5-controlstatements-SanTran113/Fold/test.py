# Name: San Tran
# Date: 10 / 21 / 22
# Github: SanTran113

import unittest
import objects
import functions

class FoldTest(unittest.TestCase):

    def test_1(self):
        pass

    def test_getMinmum_eq_1(self):
        l = [1, 2, 3, 4]
        self.assertEqual(1, functions.getMinimum(l))

    def test_getMinmum_eq_2(self):
        l = [-5, -1, 5, 1]
        self.assertEqual(-5, functions.getMinimum(l))


    def test_areAllTrue_eq_1(self):
        l = [True, True, True, True]
        self.assertTrue(True, functions.areAllTrue(l))

    def test_areAllTrue_eq_2(self):
        l = [True, True, False, True]
        self.assertFalse(False, functions.areAllTrue(l))



    def test_getCenterPoint_eq_1(self):
        p = [objects.Point(1, 2), objects.Point(3, 4), objects.Point(5, 6)]
        self.assertEqual(objects.Point(3, 4), functions.getCenterPoint(p))

    def test_getCenterPoint_eq_2(self):
        p = [objects.Point(0, 0), objects.Point(5, 10), objects.Point(10, 20)]
        self.assertEqual(objects.Point(5, 10), functions.getCenterPoint(p))


    def test_countLessThanFour_eq_1(self):
        s = ["Hellooo", "Up", "Hi", "MCC"]
        self.assertEqual(3, functions.countLessThanFour(s))

    def test_coutLessThanFour_eq_2(self):
        s = ["He", "often", "eats", "small", "steamed", "meat", "dumplings"]
        self.assertEqual(3, functions.countLessThanFour(s))

if __name__ == "__main__":
    unittest.main()
