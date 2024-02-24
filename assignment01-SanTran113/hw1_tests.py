import hw1
import unittest


class TestCases(unittest.TestCase):
    def test_Price_1(self):
        price = hw1.Price(1, 20)
        self.assertEqual(price.dollars, 1)
        self.assertEqual(price.cents, 20)

    def test_Price_2(self):
        price = hw1.Price(4, 19)
        self.assertEqual(price.dollars, 4)
        self.assertEqual(price.cents, 19)

    def test_Price_eq_1(self):
        price1 = hw1.Price(1, 20)
        price2 = hw1.Price(1, 20)
        self.assertEqual(price1, price2)

    def test_Price_eq_2(self):
        price1 = hw1.Price(1, 20)
        self.assertEqual(price1, price1)

    def test_Price_eq_3(self):
        price1 = hw1.Price(1, 20)
        price2 = hw1.Price(2, 20)
        self.assertNotEqual(price1, price2)

    def test_Price_eq_4(self):
        price1 = hw1.Price(1, 20)
        price2 = 1.20
        self.assertNotEqual(price1, price2)

    # Part 1
    def test_add_price_eq_1(self):
        price1 = hw1.Price(5, 70)
        price2 = hw1.Price(1, 80)
        p = hw1.add_price(price1, price2)
        self.assertEqual(p.cents, 50)
        self.assertEqual(p.dollars, 7)

    def test_add_price_eq_2(self):
        price1 = hw1.Price(6, 50)
        price2 = hw1.Price(4, 80)
        p = hw1.add_price(price1, price2)
        self.assertEqual(p.cents, 30)
        self.assertEqual(p.dollars, 11)


    # Part 2 & 3
    def test_Point_eq_1(self):
        point1 = hw1.Point(0, 1)
        point2 = hw1.Point(0, 1)
        self.assertEqual(point1, point2)

    def test_Point_eq_2(self):
        point1 = hw1.Point(0, 1)
        point2 = hw1.Point(0, 1)
        self.assertEqual(point1, point2)

    def test_Rectangle_eq_1(self):
        point1 = hw1.Point(0, 1)
        point2 = hw1.Point(3, 0)
        rec1 = hw1.Rectangle(point1, point2)
        rec2 = hw1.Rectangle(point1, point2)
        self.assertEqual(rec1, rec2)

    def test_Rectangle_eq_2(self):
        point1 = hw1.Point(1, 5)
        point2 = hw1.Point(6, 7)
        rec1 = hw1.Rectangle(point1, point2)
        rec2 = hw1.Rectangle(point1, point2)
        self.assertEqual(rec1, rec2)

    def test_Circle_eq_1(self):
        point1 = hw1.Circle(hw1.Point(0, 2), 4)
        point2 = hw1.Circle(hw1.Point(0, 2), 4)
        self.assertEqual(point1, point2)

    def test_Circle_eq_2(self):
        point1 = hw1.Circle(hw1.Point(0, 3), 6)
        point2 = hw1.Circle(hw1.Point(0, 3), 6)
        self.assertEqual(point1, point2)

    # Part 4
    def test_rectangle_perimeter_eq_1(self):
        point1 = hw1.Point(1, 5)
        point2 = hw1.Point(3, 1)
        rectangle = hw1.Rectangle(point1, point2)
        self.assertEqual(hw1.rectangle_perimeter(rectangle), 12)

    def test_rectangle_perimeter_eq_2(self):
        point1 = hw1.Point(2, 5)
        point2 = hw1.Point(6, 1)
        rectangle = hw1.Rectangle(point1, point2)
        self.assertEqual(hw1.rectangle_perimeter(rectangle), 16)

    # Part 5
    def test_rectangle_Lower_half_eq_1(self):
        point1 = hw1.Point(0, 5)
        point2 = hw1.Point(3, 0)
        rectangle = hw1.Rectangle(point1, point2)
        point3 = hw1.Point(0, 2.5)
        point4 = hw1.Point(3, 0)
        rectangle2 = hw1.Rectangle(point3, point4)
        one = hw1.rectangle_Lower_half(rectangle)
        self.assertEqual(one, rectangle2)

    def test_rectangle_Lower_half_eq_2(self):
        point1 = hw1.Point(1, 10)
        point2 = hw1.Point(2, 1)
        rectangle = hw1.Rectangle(point1, point2)
        point3 = hw1.Point(1, 5)
        point4 = hw1.Point(2, 1)
        rectangle2 = hw1.Rectangle(point3, point4)
        one = hw1.rectangle_Lower_half(rectangle)
        self.assertEqual(one, rectangle2)

    # Part 6
    def test_is_square_eq_1(self):
        point1 = hw1.Point(0, 5)
        point2 = hw1.Point(5, 0)
        rec = hw1.Rectangle(point1, point2)
        result = hw1.is_square(rec)
        self.assertTrue(result)

    def test_is_square_eq_2(self):
        point1 = hw1.Point(0, 10)
        point2 = hw1.Point(10, 0)
        rec = hw1.Rectangle(point1, point2)
        result = hw1.is_square(rec)
        self.assertTrue(result)

    # Part 7
    def test_circle_within_rectangle_eq_1(self):
        point1 = hw1.Point(0, 4)
        point2 = hw1.Point(4, 0)
        rec1 = hw1.Rectangle(point1, point2)
        center1 = hw1.Point(0, 2)
        circle = hw1.Circle(center1, 2)
        result = hw1.circle_within_rectangle(circle, rec1)
        self.assertFalse(result)

    def test_circle_within_rectangle_eq_2(self):
        point1 = hw1.Point(1, 5)
        point2 = hw1.Point(10, 0)
        rec1 = hw1.Rectangle(point1, point2)
        center1 = hw1.Point(7, 3)
        circle = hw1.Circle(center1, 6)
        result = hw1.circle_within_rectangle(circle, rec1)
        self.assertFalse(result)

    # Part 8
    def test_circle_bound_eq_1(self):
        point1 = hw1.Point(1, 1)
        point2 = hw1.Point(5, 3)
        rec1 = hw1.Rectangle(point1, point2)
        circle1 = hw1.Circle(hw1.Point(3, 2), 2.2360679774998)
        result = hw1.circle_bound(rec1)
        self.assertEqual(result, circle1)

    def test_circle_bound_eq_2(self):
        point1 = hw1.Point(0, 4)
        point2 = hw1.Point(4, 0)
        rec1 = hw1.Rectangle(point1, point2)
        circle1 = hw1.Circle(hw1.Point(2, 2), 2.8284271247462)
        result = hw1.circle_bound(rec1)
        self.assertEqual(result, circle1)



if __name__ == '__main__':
    unittest.main()
