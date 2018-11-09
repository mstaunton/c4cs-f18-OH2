import unittest

import rpn

class TestBasics(unittest.TestCase):
    def test_add(self):
        result = rpn.calculate("1 1 +")
        self.assertEqual(2, result)
    def test_subtract(self):
        result = rpn.calculate("5 3 -")
        self.assertEqual(2, result)
    def test_multiply(self):
        result = rpn.calculate("5 3 *")
        self.assertEqual(15, result)
    def test_divide(self):
        result = rpn.calculate("6 3 /")
        self.assertEqual(2, result)
    def test_exponent_1(self):
        result = rpn.calculate("3 2 ^")
        self.assertEqual(9, result)
    def test_exponent_2(self):
        result = rpn.calculate("5 3 ^")
        self.assertEqual(125, result)
    def test_intdiv_1(self):
        result = rpn.calculate("7 2 //")
        self.assertEqual(3, result)
    def test_intdiv_2(self):
        result = rpn.calculate("8 4 //")
        self.assertEqual(2, result)
    def test_factorial_1(self):
        result = rpn.calculate("4 !")
        self.assertEqual(24, result)
    def test_factorial_2(self):
        result = rpn.calculate("1 !")
        self.assertEqual(1, result)
    def test_factorial_3(self):
        result = rpn.calculate("2 !")
        self.assertEqual(2, result)
    def test_factorial_4(self):
        result = rpn.calculate("6 !")
        self.assertEqual(240, result)

