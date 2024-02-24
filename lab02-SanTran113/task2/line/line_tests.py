#San Tran
import unittest
import line

# How can we access the definition of Line?
# Import the line module here.

class LineTests(unittest.TestCase):
    def test_line(self):
        # The following line should show a warning on the value "shoe".
        result = line.Line("shoe", 2, 3, 4)
        self.assertEqual(result.x1, 1)
        self.assertEqual(result.y1, 2)
        self.assertEqual(result.x2, 3)
        self.assertEqual(result.y2, 4)

    def test_line_again(self):
        result = line.Line(2, 3, 4, 5)
        self.assertEqual(result.x1, 2)
        self.assertEqual(result.y1, 3)
        self.assertEqual(result.x2, 4)
        self.assertEqual(result.y2, 5)

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()
