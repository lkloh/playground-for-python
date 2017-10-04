# Copied tests from https://docs.python.org/2/library/unittest.html
# RUN: python3 patch_class.py
import random
import unittest
from unittest.mock import patch

class TestStringMethods(unittest.TestCase):

    @classmethod
    @patch.object(random, 'random')
    def setUp(cls, mock):
        mock.return_value = 0.5
        print(random.random())

    def test_one(self):
        print(random.random())

    def test_two(self):
        print(random.random())

    def test_three(self):
        print(random.random())

if __name__ == '__main__':
    unittest.main()
