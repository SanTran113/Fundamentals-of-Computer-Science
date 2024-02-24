# Name:
# Date:
# Github:

import unittest
import math
import hw2

class AssignmentTests(unittest.TestCase):
    # The following test must not be modified and pass
    def test_Duration_init_1(self):
        duration = hw2.Duration(60, 0)
        self.assertEqual(duration.minutes, 60)
        self.assertEqual(duration.seconds, 0)

    def test_Duration_init_2(self):
        duration = hw2.Duration(0, 30)
        self.assertEqual(duration.minutes, 0)
        self.assertEqual(duration.seconds, 30)

    def test_Duration_init_3(self):
        duration = hw2.Duration(15, 15)
        self.assertEqual(duration.minutes, 15)
        self.assertEqual(duration.seconds, 15)

    def test_Duration_eq_1(self):
        duration = hw2.Duration(60, 0)
        self.assertEqual(duration, duration)

    def test_Duration_eq_2(self):
        duration_1 = hw2.Duration(60, 0)
        duration_2 = hw2.Duration(60, 0)
        self.assertEqual(duration_1, duration_2)

    def test_Duration_eq_3(self):
        duration = hw2.Duration(60, 0)
        point = hw2.Point(60, 0)
        self.assertNotEqual(duration, point)

    def test_Point_init_1(self):
        point = hw2.Point(5, 5)
        self.assertEqual(point.x, 5)
        self.assertEqual(point.y, 5)

    def test_Point_init_2(self):
        point = hw2.Point(0, 10)
        self.assertEqual(point.x, 0)
        self.assertEqual(point.y, 10)

    def test_Point_init_3(self):
        point = hw2.Point(10, 0)
        self.assertEqual(point.x, 10)
        self.assertEqual(point.y, 0)

    def test_Point_eq_1(self):
        point = hw2.Point(15, 15)
        self.assertEqual(point, point)

    def test_Point_eq_2(self):
        point_1 = hw2.Point(15, 15)
        point_2 = hw2.Point(15, 15)
        self.assertEqual(point_1, point_2)

    def test_Point_eq_3(self):
        point = hw2.Point(15, 15)
        duration = hw2.Duration(15, 15)
        self.assertNotEqual(point, duration)

    def test_Rectangle_init_1(self):
        rectangle = hw2.Rectangle(hw2.Point(0, 5), hw2.Point(5, 0))
        self.assertEqual(rectangle.top_left.x, 0)
        self.assertEqual(rectangle.top_left.y, 5)
        self.assertEqual(rectangle.bottom_right.x, 5)
        self.assertEqual(rectangle.bottom_right.y, 0)

    def test_Rectangle_eq_1(self):
        rectangle = hw2.Rectangle(hw2.Point(0, 5), hw2.Point(5, 0))
        self.assertEqual(rectangle, rectangle)

    def test_Rectangle_eq_2(self):
        rectangle_1 = hw2.Rectangle(hw2.Point(0, 5), hw2.Point(5, 0))
        rectangle_2 = hw2.Rectangle(hw2.Point(0, 5), hw2.Point(5, 0))
        self.assertEqual(rectangle_1, rectangle_2)

    def test_Rectangle_eq_3(self):
        rectangle = hw2.Rectangle(hw2.Point(0, 0), hw2.Point(5, 0))
        duration = hw2.Duration(15, 15)
        self.assertNotEqual(rectangle, duration)

    def test_Triangle_init_1(self):
        triangle = hw2.Triangle(hw2.Point(0, 0), hw2.Point(5, 5), hw2.Point(10, 0))
        self.assertEqual(triangle.a.x, 0)
        self.assertEqual(triangle.a.y, 0)
        self.assertEqual(triangle.b.x, 5)
        self.assertEqual(triangle.b.y, 5)
        self.assertEqual(triangle.c.x, 10)
        self.assertEqual(triangle.c.y, 0)

    def test_Triangle_eq_1(self):
        triangle = hw2.Triangle(hw2.Point(0, 0), hw2.Point(5, 5), hw2.Point(10, 0))
        self.assertEqual(triangle, triangle)

    def test_Triangle_eq_2(self):
        triangle_1 = hw2.Triangle(hw2.Point(0, 0), hw2.Point(5, 5), hw2.Point(10, 0))
        triangle_2 = hw2.Triangle(hw2.Point(0, 0), hw2.Point(5, 5), hw2.Point(10, 0))
        self.assertEqual(triangle_1, triangle_2)

    def test_Triangle_eq_3(self):
        triangle = hw2.Triangle(hw2.Point(0, 0), hw2.Point(5, 5), hw2.Point(10, 0))
        duration = hw2.Duration(15, 15)
        self.assertNotEqual(triangle, duration)

    # Implement your tests here:

    def test_isShorterThan_eq_1(self):
        x = hw2.Duration(4, 23)
        y = hw2.Duration(4, 50)
        self.assertTrue(x, y)

    def test_isShorterThan_eq_2(self):
        x = hw2.Duration(9, 50)
        y = hw2.Duration(8, 50)
        self.assertFalse(hw2.isShorterThan(x, y))



    def test_triangulateRectangle_eq_1(self):
        r = hw2.Rectangle(hw2.Point(0, 5), hw2.Point(10, 0))
        self.assertEqual([hw2.Triangle(hw2.Point(0,5),hw2.Point(10,0),hw2.Point(0,0)), hw2.Triangle(hw2.Point(0,5),hw2.Point(10,0),hw2.Point(10,5))],
                         hw2.triangualteRectangle(r))

    def test_triangulateRectangle_eq_2(self):
        r = hw2.Rectangle(hw2.Point(-1, -10), hw2.Point(-10, -5))
        self.assertEqual([hw2.Triangle(hw2.Point(-1, -10), hw2.Point(-10, -5), hw2.Point(-1, -5)), hw2.Triangle(hw2.Point(-1, -10), hw2.Point(-10,-5), hw2.Point(-10,-10))],
                         hw2.triangualteRectangle(r))



    def test_createRectangle_eq_1(self):
        p1 = hw2.Point(10,0)
        p2 = hw2.Point(0,5)
        self.assertEqual(hw2.Rectangle(hw2.Point(0, 5), hw2.Point(10, 0)), hw2.createRectangle(p1, p2))

    def test_createRectangle_eq_2(self):
        p1 = hw2.Point(-10, 5)
        p2 = hw2.Point(-1, 0)
        self.assertEqual(hw2.Rectangle(hw2.Point(-10, 5), hw2.Point(-1, 0)), hw2.createRectangle(p1, p2))



    def test_addDurations_eq_1(self):
        x = hw2.Duration(7, 50)
        y = hw2.Duration(8, 50)
        self.assertEqual(hw2.Duration(16, 40), hw2.addDurations(x, y))

    def test_addDurations_eq_2(self):
        x = hw2.Duration(7, 0)
        y = hw2.Duration(8, 30)
        self.assertEqual(hw2.Duration(15, 30), hw2.addDurations(x, y))



    def test_getLengthsInSeconds_eq_1(self):
        l = [hw2.Song("Everybody Wants to Rule the World", "Tears For Fears", hw2.Duration(4, 11)),
             hw2.Song("River Flows In You", "Yiruma", hw2.Duration(3, 8))]
        self.assertEqual([251,188], hw2.getLengthsInSeconds(l))

    def test_getLengthsInSeconds_eq_2(self):
        l = [hw2.Song("Wish of the Song Bird", "Enna Alouette", hw2.Duration(5, 57)),
             hw2.Song("Tsunami", "Finana Ryugu", hw2.Duration(3, 17))]
        self.assertEqual([357, 197], hw2.getLengthsInSeconds(l))


    # help
    def test_getSongByArtist_eq_1(self):
        l = [hw2.Song("Everybody Wants to Rule the World", "Tears For Fears", hw2.Duration(4, 11)),
             hw2.Song("River Flows In You", "Yiruma", hw2.Duration(3, 8))]
        a = 'Tears For Fears'
        self.assertEqual([hw2.Song("Everybody Wants to Rule the World", "Tears For Fears", hw2.Duration(4, 11))], hw2.getSongByArtist(l, a))

    def test_getSongByArtist_eq_2(self):
        l = [hw2.Song("Wish of the Song Bird", "Enna Alouette", hw2.Duration(5, 57)),
            hw2.Song("Tsunami", "Finana Ryugu", hw2.Duration(3, 17))]
        a = "Enna Alouette"
        self.assertEqual([hw2.Song("Wish of the Song Bird", "Enna Alouette", hw2.Duration(5, 57))], hw2.getSongByArtist(l, a))



    def test_getPlayListLength_eq_1(self):
        l = [hw2.Song("Everybody Wants to Rule the World", "Tears For Fears", hw2.Duration(4, 11)), hw2.Song("River Flows In You", "Yiruma", hw2.Duration(3, 8))]
        self.assertEqual(hw2.getPlayListLength(l), hw2.Duration(7, 19))

    def test_getPlayListLength_eq_2(self):
        l = [hw2.Song("Everybody Wants to Rule the World", "Tears For Fears", hw2.Duration(4, 50)), hw2.Song("River Flows In You", "Yiruma", hw2.Duration(3, 50))]
        self.assertEqual(hw2.getPlayListLength(l), hw2.Duration(8, 40))

if __name__ == "__main__":
    unittest.main()
