import pytest
import unittest

class TestStringMethods(unittest.TestCase):
    def test_upper(self):
        self.assertEqual('marcelo'.upper(), 'MARCELO')