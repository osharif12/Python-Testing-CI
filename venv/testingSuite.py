# python3 -m unittest testingSuite.TestAddition
# python3 -m unittest testingSuite.py

import unittest
from utilFunctions import *


class TestAddition(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.ds = UtilFunctions()

    def test_addition(self):
        value = self.ds.add_numbers(198, 2)

        assert value == 200

    def test_negative_addition(self):
        value = self.ds.add_numbers(-45, -66)

        assert value == -111


class TestSubtraction(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.ds = UtilFunctions()

    def test_addition(self):
        value = self.ds.subtract_numbers(198, 2)

        assert value == 196

    def test_negative_addition(self):
        value = self.ds.subtract_numbers(-45, 66)

        assert value == -111