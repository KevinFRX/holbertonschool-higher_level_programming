#!/usr/bin/python3
"""Unittest for max_integer([...])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Unittest class for max_integer"""
    def test_normal(self):
        """Test with normal values"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_with_strings(self):
        """Test with strings in the list"""
        with self.assertRaises(TypeError):
            max_integer([1, 2, 3, "XD"])

    def test_empty(self):
        """Test with an empty string"""
        self.assertEqual(max_integer([]), None)
