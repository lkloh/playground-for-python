# Copied tests from https://docs.python.org/2/library/unittest.html
# RUN: python3 patch_class.py
import random
import unittest
from unittest.mock import patch

class TestPatchSetup(unittest.TestCase):

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

@patch.object(random, 'random')
class TestPatchClass(unittest.TestCase):

    def setUp(self):
        self.patch_random = patch('random.random')
        self.mock_random = self.patch_random.start()
        self.mock_random.return_value = 0.5
        self.addCleanup(self.patch_random.stop)

    def test_one(self, mock):
        print(random.random())

    def test_two(self, mock):
        print(random.random())

    def test_three(self, mock):
        print(random.random())

if __name__ == '__main__':
    unittest.main()
