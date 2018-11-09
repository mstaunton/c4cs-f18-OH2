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
        self.assertEqual(720, result)
    def test_factorial_5(self):
        result = rpn.calculate("-1 !")
        self.assertEqual("Error: Factorial only on positive numbers", result)
    def test_div_by_zero_1(self):
        result = rpn.calculate("9 0 /")
        self.assertEqual("Error: Cannot divide by Zero, Try again", result)
    def test_div_by_zero_2(self):
        result = rpn.calculate("240 0 //")
        self.assertEqual("Error: Cannot divide by Zero, Try again", result)
    def test_repeat_operator_1(self):
        result = rpn.calculate("2 5 10 + !")
        self.assertEqual(17, result)
    def test_repeat_operator_2(self):
        result = rpn.calculate("5 2 3 10 * !")
        self.assertEqual(300, result)
    def test_repeat_operator_3(self):
        result = rpn.calculate("20 5 4 / !")
        self.assertEqual(1, result)
    def test_repeat_operator_4(self):
        result = rpn.calculate("10 5 12 -3 - !")
        self.assertEqual(-4, result)


