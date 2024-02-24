# San Tran
import unittest
import objects
import funcs_objects


class TestCases(unittest.TestCase):
    def test_point(self):
        center = objects.Point(1, 2)
        self.assertEqual(center.x, 1)
        self.assertEqual(center.y, 2)

    def test_distance(self):
        A = objects.Point(1, 2)
        B = objects.Point(3, 4)
        result = funcs_objects.distance(A, B)
        # result is the distance from point A to point B = 2.8284271247461903
        self.assertEqual(result, 2.8284271247461903)

    def test_distance2(self):
        J = objects.Point(1, 13)
        K = objects.Point(14, 15)
        result2 = funcs_objects.distance(J, K)
        self.assertEqual(result2, 13.152946437965905)


    def test_circle(self):
        A = objects.Point(0, 0)
        one = objects.Circle(A, 8)
        B = objects.Point(15, 0)
        two = objects.Circle(B, 7)
        T = funcs_objects.circles_overlap(one, two)
        result = T
        self.assertFalse(result, False)

    def test_circle2(self):
        A = objects.Point(4, 5)
        one = objects.Circle(A, 4)
        B = objects.Point(6, 7)
        two = objects.Circle(B, 4)
        T = funcs_objects.circles_overlap(one, two)
        result = T
        self.assertTrue(result, True)


# Run the unit tests.
if __name__ == '__main__':
    unittest.main()
