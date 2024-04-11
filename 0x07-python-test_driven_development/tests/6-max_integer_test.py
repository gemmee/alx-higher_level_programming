#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max(self):
        self.assertEqual(max_integer([-99, 0, 2]), 2)
        self.assertEqual(max_integer([-11]), -11)
        self.assertEqual(max_integer([1, 1, 0]), 1)


    def test_empty(self):
        self.assertEqual(max_integer([]), None)

