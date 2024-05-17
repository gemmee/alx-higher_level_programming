#!/usr/bin/python3
# test_base.py
"""
Defines unittests for base module (base.py).

Unittest classes:
    TestBase_instantiation

"""
import unittest
from models.base import Base


class TestBase_instantiation(unittest.TestCase):
    """
    Unittests for testing instantiation of the Base class.
    """

    def test_no_arg(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_three_bases(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 2)

    def test_None_id(self):
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b1.id, b2.id - 1)

    def test_unique_id(self):
        self.assertEqual(13, Base(13).id)

    def test_nb_instances_after_unique_id(self):
        b1 = Base()
        b2 = Base(13)
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 1)

    def test_id_public(self):
        b = Base(14)
        b.id = 16
        self.assertEqual(16, b.id)

    def test_nb_instances_private(self):
        with self.assertRaises(AttributeError):
            print(Base(13).__nb_instances)

    def test_str_id(self):
        self.assertEqual("akkam", Base("akkam").id)

    def test_float_id(self):
        self.assertEqual(4.5, Base(4.5).id)

    def test_complex_id(self):
        self.assertEqual(3j, Base(3j).id)

    def test_bool_id(self):
        self.assertEqual(True, Base(True).id)

    def test_dict_id(self):
        self.assertEqual({1: "a", 2: "b"}, Base({1: "a", 2: "b"}).id)

    def test_list_id(self):
        self.assertEqual([3, 2, 3], Base([3, 2, 3]).id)

    def test_tuple_id(self):
        self.assertEqual((3, 2), Base((3, 2)).id)

    def test_set_id(self):
        self.assertEqual({1, 2}, Base({1, 2}).id)

    def test_frozenset_id(self):
        self.assertEqual(frozenset({1, 2}), Base(frozenset({1, 2})).id)

    def test_range_id(self):
        self.assertEqual(range(5), Base(range(5)).id)

    def test_bytes_id(self):
        self.assertEqual(b'Python', Base(b'Python').id)

    def test_bytearray_id(self):
        self.assertEqual(bytearray(b'gamachu'), Base(bytearray(b'gamachu')).id)

    def test_memoryview_id(self):
        self.assertEqual(memoryview(b'gamachu'),
                         Base(memoryview(b'gamachu')).id)

    def test_inf_id(self):
        self.assertEqual(float('inf'), Base(float('inf')).id)

    def test_NaN_id(self):
        self.assertNotEqual(float('nan'), Base(float('nan')).id)

    def test_two_args(self):
        with self.assertRaises(TypeError):
            Base(4, 3)
