#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max(self):
        # max element at the beginning
        self.assertEqual(max_integer([99, 98, 34]), 99)
        # max element at the end
        self.assertEqual(max_integer([9, 39, 100]), 100)
        # max element in the middle
        self.assertEqual(max_integer([9, 49, 30, 20]), 49)
        # one negative number in the list
        self.assertEqual(max_integer([-99, 0, 2]), 2)
        # only negative number in the list
        self.assertEqual(max_integer([-100, -200, -300]), -100)
        # list of one element
        self.assertEqual(max_integer([-11]), -11)
        # duplicate elements in the list
        self.assertEqual(max_integer([1, 1, 0, 0]), 1)


    def test_empty(self):
        # list is empty
        self.assertEqual(max_integer([]), None)

