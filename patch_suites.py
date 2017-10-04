
import random
import math
import unittest
from unittest.mock import patch

class TestPatchClass(unittest.TestCase):

    def test_one(self):
        print(random.random())

    def test_two(self):
        print(random.random())

    def test_three(self):
        print(random.random())

if __name__ == '__main__':
    # unittest.TextTestRunner().run(unittest.makeSuite(TestPatchClass))

    with patch.object(random, 'random') as mock_random:
        mock_random.return_value = 0.5
        unittest.TextTestRunner().run(unittest.makeSuite(TestPatchClass))

    with patch.object(random, 'random') as mock_random:
        mock_random.return_value = 0.7
        unittest.TextTestRunner().run(unittest.makeSuite(TestPatchClass))