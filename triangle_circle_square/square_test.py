import unittest

from square import *


class Square_test(unittest.TestCase):
    def test_triangle(self):
        self.t = Square.triangle(4, 5, 6)
        self.assertEqual(self.t.square, 9.92)
    def test_right_triangle(self):
        self.t = Square.triangle(12, 15, 9)
        self.assertTrue(self.t._right_triangle)

    def test_circle(self):
        self.t = Square.circle(4)
        self.assertEqual(self.t.square,50.27)
        self.assertEqual(self.t._right_triangle, None)

    def test_i_dont_know_what_this(self):
        self.t = Square.i_dont_know_what_this(4, 5, 6)
        self.assertEqual(self.t.square, 9.92)
        self.t = Square.i_dont_know_what_this(4)
        self.assertEqual(self.t.square, 50.27)
        self.t = Square.i_dont_know_what_this(4, 5, 6,8)
        self.assertEqual(self.t, "I don't know what it is either")


