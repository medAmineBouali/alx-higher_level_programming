#!/usr/bin/python3
"""module for testing base"""
import unittest
from models.base import Base

class TestsBase(unittest.TestCase):
    """Tests the base model"""

    def test_valid_id(self):
        """Tests for a valid id"""
        b1 = Base()
        self.assertEqual(b1.id, 1)

    def test_is_valid_string(self):
        """Testing fo string inputs"""
        b2 = Base("ALX")
        self.assertEqual(b2.id, "ALX")
