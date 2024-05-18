#!/usr/bin/python3
# test_rectangle.py
"""
Defines unittests for models/rectangle.py.

"""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Rectangle class.
    """

    def test_rectangle_is_base(self):
        self.assertIsInstance(Rectangle(10, 2), Base)

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_one_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_two_args(self):
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        self.assertEqual(r1.id, r2.id - 1)

    def test_three_args(self):
        r1 = Rectangle(2, 2, 4)
        r2 = Rectangle(4, 4, 2)
        self.assertEqual(r1.id, r2.id - 1)

    def test_four_args(self):
        r1 = Rectangle(1, 2, 3, 4)
        r2 = Rectangle(4, 3, 2, 1)
        self.assertEqual(r1.id, r2.id - 1)

    def test_five_args(self):
        self.assertEqual(8, Rectangle(3, 4, 5, 6, 8).id)

    def test_more_than_five_args(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4, 5, 6)

    def test_width_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(4, 5).__width)

    def test_height_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(4, 5).__height)

    def test_x_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(4, 5, 1, 2).__x)

    def test_y_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(4, 5, 1, 2).__y)

    def test_width_getter(self):
        r = Rectangle(4, 5)
        self.assertEqual(4, r.width)

    def test_width_setter(self):
        r = Rectangle(4, 5)
        r.width = 10
        self.assertEqual(10, r.width)

    def test_height_getter(self):
        r = Rectangle(4, 5)
        r.height = 11
        self.assertEqual(11, r.height)

    def test_x_getter(self):
        r = Rectangle(4, 5, 1, 2)
        self.assertEqual(1, r.x)

    def test_x_setter(self):
        r = Rectangle(4, 5, 1, 2)
        r.x = 3
        self.assertEqual(3, r.x)

    def test_y_getter(self):
        r = Rectangle(4, 5, 1, 2)
        self.assertEqual(2, r.y)

    def test_y_setter(self):
        r = Rectangle(4, 5, 1, 2)
        r.y = 4
        self.assertEqual(4, r.y)
