# Name: San Tran
# Date: 10/ 3 / 22
# Github: SanTran113

import unittest
import functions

class LabTest(unittest.TestCase):
    # The following test is an example of using the unittest framework for the
    #   addValues function.
    def testAddValues(self):
        self.assertEqual(functions.addValues(2, 3), 5)
        self.assertEqual(functions.addValues(6, 3), 9)
        self.assertEqual(functions.addValues(-19, 34), 15)

    # Write your tests following this comment. An empty test is given as
    #   an example. This function's name should be appropriately changed and
    #   the included "pass" statement is place-holder code that may be removed
    #   once your test is implemented.
    def test_getSquareRoot(self):
        self.assertEqual(functions.getSquareRoot(9), 3)
        self.assertEqual(functions.getSquareRoot(36), 6)
    def test_convertToCelius(self):
        self.assertAlmostEqual(functions.convertToCelsius(73), 22.77777777777778)
        self.assertAlmostEqual(functions.convertToCelsius(103), 39.44444444444444)
    def test_capitalizeCharacter(self):
        self.assertEqual(functions.capitalizeCharacter("san",1), "San")
        self.assertEqual(functions.capitalizeCharacter("tran",1), "Tran")

if __name__ == "__main__":
    unittest.main()
