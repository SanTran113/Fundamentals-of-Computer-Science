# Name: San Tran
# Date: 10 / 24 / 22
# GitHub: SanTran113

import unittest
import functions

class CharacterTest(unittest.TestCase):

    def test_isEnglishUpper_eq_1(self):
        char = "Banana"
        self.assertTrue(functions.isEnglishUpper(char))

    def test_isEnglishUpper_eq_2(self):
        char = "carrot"
        self.assertFalse(functions.isEnglishUpper(char))

if __name__ == "__main__":
    unittest.main()
