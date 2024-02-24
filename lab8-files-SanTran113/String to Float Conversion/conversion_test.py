# Name: San Tran
# Date: 11 / 9 / 22
# GitHub: SanTran113
import unittest
import conversion


class MyTestCase(unittest.TestCase):
    # def test_something(self):
    #     self.assertEqual(True, False)  # add assertion here

    def test_stringToFloat_eq_1(self):
        in_ = "1.45"
        self.assertEqual(1.45, conversion.stringToFloat(in_))

    def test_stringToFloat_eq_2(self):
        in_ = "1.45abc"
        self.assertEqual(None, conversion.stringToFloat(in_))


if __name__ == '__main__':
    unittest.main()
