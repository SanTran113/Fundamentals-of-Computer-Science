# Name: San Tran
# Date: 10 / 24 / 22
# GitHub: SanTran113

import unittest
import functions

class StringTest(unittest.TestCase):

    def test_swapCase_eq_1(self):
        input = "EarPhoneCase"
        self.assertEqual("eARpHONEcASE", functions.swapCase(input))

    def test_swapCase_eq_2(self):
        input = "EarPhoneCase♁♁♁"
        self.assertEqual("eARpHONEcASE♁♁♁", functions.swapCase(input))

    def  test_replaceChar_eq_1(self):
        input = "peanuts"
        from1 = "p"
        to = "b"
        self.assertEqual("beanuts", functions.replaceChar(input, from1, to))

    def test_replaceChar_eq_2(self):
        input = "nautrality"
        from1 = "aa"
        to = "e"
        self .assertEqual("nautrality", functions.replaceChar(input, from1, to))

if __name__ == "__main__":
    unittest.main()
