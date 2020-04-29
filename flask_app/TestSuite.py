import unittest
from app import test_method

class TestSuite(unittest.TestCase):

    def setUp(self):
        self.Test = TestSuite()

    def test_True(self):
        self.assertTrue(test_method(True))

    def test_False(self):
        self.assertFalse(test_method(True))