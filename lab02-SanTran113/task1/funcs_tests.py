#San Tran

import unittest
import math

class TestCases(unittest.TestCase):
   def test_f_1(self):
      # Add code here.
      self.fail("Test not implemented")


   def test_f_2(self):
      # Add code here.
      self.fail("Test not implemented")


# Run the unit tests.

class function1(unittest.TestCase):
   def test_f(self):
      x=1
      self.assertAlmostEqual(7*x**2+2*x,9)

   def test_g(self):
      x=1
      y=1
      self.assertAlmostEqual(x**2+y**2, 2)

   def test_hypotenuse(self):
      x=1
      y=1
      self.assertAlmostEqual(math.sqrt(x**2+y**2), math.sqrt(2))

   def test_is_positive(self):
      x=1
      self.assertTrue(x >= 0, "true")

if __name__ == '__main__':
   unittest.main()

