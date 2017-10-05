


import random
import math
import unittest


class TestPatchClass(unittest.TestCase):

    def test_one(self):
    	self.helper()
        print(random.random())

    def test_two(self):
    	self.helper()
        print(random.random())

    def test_three(self):
    	self.helper()
        print(random.random())

    def helper(self):
        print('I am a helper\n\n')


if __name__ == '__main__':
    unittest.main()
