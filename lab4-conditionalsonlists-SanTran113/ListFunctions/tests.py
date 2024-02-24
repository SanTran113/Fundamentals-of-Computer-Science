# Name: San Tran
# Date: 10 / 10 / 2022
# Github: SanTran113

import unittest
import functions

class listFunctionTests(unittest.TestCase):
    # Do not modify these tests
    def test_includedOne(self):
        self.assertTrue(functions.areTwoEqual([1, 2, 3, 2], 1, 3))
        self.assertFalse(functions.areTwoEqual([1, 2, 3, 2], 1, 2))

    def test_includedTwo(self):
        self.assertEqual(functions.sumOfThree([1, 2, 3, 2]), 0)
        self.assertEqual(functions.sumOfThree([1, 2]), 0)
        self.assertEqual(functions.sumOfThree([1, 2, 3]), 6)

    def test_includedThree(self):
        self.assertEqual(functions.sumOfUpToThree([1, 2, 3, 2]), 6)
        self.assertEqual(functions.sumOfUpToThree([1, 2]), 3)
        self.assertEqual(functions.sumOfUpToThree([1, 2, 3]), 6)

    def test_includedFour(self):
        self.assertEqual(functions.getFromFirstAsIndex([1, 2, 3, 2]), 2)
        self.assertEqual(functions.getFromFirstAsIndex([2, 2, 3, 2]), 3)
        self.assertEqual(functions.getFromFirstAsIndex([-1, 2, 3, 2]), 2)

    # Write your tests below
    def test_areTwoEqual_1(self):
        self.assertTrue(functions.areTwoEqual([4, 5, 0, 4], 0, 3))
        self.assertFalse(functions.areTwoEqual([1, 6], 0, 1))
    def test_areTwoEqual_2(self):
        self.assertTrue(functions.areTwoEqual([6, 6], 0, 1))
        self.assertFalse(functions.areTwoEqual([4, 5, 0, 4], 0, 2))

    def test_sumOfThree_1(self):
        self.assertEqual(functions.sumOfThree([0, 0, 1]), 1)
        self.assertEqual(functions.sumOfThree([4, 5]), 0)

    def test_sumOfThree_2(self):
        self.assertEqual(functions.sumOfThree([1, 7, 4]), 12)
        self.assertEqual(functions.sumOfThree([0, 0, 1, 4, 5]), 0)

    def test_sumOfUpToThree_1(self):
        self.assertEqual(functions.sumOfUpToThree([1, 2]), 3)
        self.assertEqual(functions.sumOfUpToThree([1, 8, 2, 7, 8]), 11)

    def test_sumOfUpToThree_2(self):
        self.assertEqual(functions.sumOfUpToThree([1, 2, 7]), 10)
        self.assertEqual(functions.sumOfUpToThree([7]), 7)

    def test_getFromFirstAsIndex_1(self):
        self.assertEqual(functions.getFromFirstAsIndex([1, 2, 3, 4]), 2)
        self.assertEqual(functions.getFromFirstAsIndex([4, 4, 4, 4, 4]), 4)

    def test_getFromFirstAsIndex_2(self):
        self.assertEqual(functions.getFromFirstAsIndex([3, 1, 1, 1]), 1)
        self.assertEqual(functions.getFromFirstAsIndex([2, 3, 17, 8, 9]), 17)

if __name__ == "__main__":
    unittest.main()
