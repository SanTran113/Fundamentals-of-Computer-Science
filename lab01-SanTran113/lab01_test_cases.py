# San Tran
# Test cases example for lab 1.
#

import unittest # import the module that supports writing unit tests

# Define a class that will be used for these test cases.
# This class will include testing functions.
#
# We will explain what the is code does in lecture.
#
def assertAlmostEqual(x, y):
    pass


class TestsLab1(unittest.TestCase):

    # Define one testing function per test.
    def test_expression_1(self):
        self.assertAlmostEqual(0 + 1, 1)


    def test_expression_2(self):
        self.assertAlmostEqual(2 * 2, 4)

    # Add additional tests below

    def test_expression_3(self):
        self.assertEqual(19//3, 6.333333333333333)

    def test_expression_4(self):
          self.assertAlmostEqual(19/3, 6.333333333333333)

    def test_expression_3(self):
          self.assertAlmostEqual(19/3.0, 6.333333333333333)

    def test_expression_3(self):
          self.assertAlmostEqual(19.0/3.0, 6.333333333333333)

    def test_expression_3(self):
          self.assertAlmostEqual(4*2+27//3+4, 21)

    def test_expression_3(self):
          self.assertAlmostEqual(4*(2+27)//3+4, 42)

    def test_expression_3(self):
        x=1
        y=2
        self.assertAlmostEqual(2*x+y,4)

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

