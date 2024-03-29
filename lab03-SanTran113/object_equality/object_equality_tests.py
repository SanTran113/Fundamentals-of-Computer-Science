import unittest
import point


class TestCases(unittest.TestCase):
    def test_point_one(self):
        pt = point.Point(1, 2)
        self.assertEqual(pt.x, 1)
        self.assertEqual(pt.y, 2)

    def test_point_two(self):
        pt = point.Point(-4.7, 19.2)
        self.assertEqual(pt.x, -4.7)
        self.assertEqual(pt.y, 19.2)

    def test_equality_one(self):
        # Replace pass with the test code.
        pass

    def test_equality_two(self):
        # Replace pass with the test code.
        pass


# Run the unit tests.
if __name__ == '__main__':
    unittest.main()
