# Name: San Tran
# Date: 11 / 4 / 22
# GitHub: SanTran113

import unittest

import histogram


class Histogram(unittest.TestCase):
    # def test_something(self):
        # self.assertEqual(True, False)  # add assertion here


    def test_getHistogram_eq_1(self):
        input = "sauce bread sauce cheese tomato patty sauce bread"
        self.assertEqual({'bread': 2, 'cheese': 1, 'patty': 1, 'sauce': 3, 'tomato': 1}, histogram.getHistogram(input))

    def test_getHistogram_eq_2(self):
        input = "I love love love my family and friends"
        self.assertEqual({'I': 1, 'and': 1, 'family': 1, 'friends': 1, 'love': 3, 'my': 1}, histogram.getHistogram(input))

if __name__ == '__main__':
    unittest.main()
