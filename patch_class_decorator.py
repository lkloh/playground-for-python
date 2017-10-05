

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


def decorator(cls):
	class Wrapper(object):
		def __init__(self, *args):
			self.wrapped = cls(*args)

		@patch.object(random, 'random')
		def __getattr__(self, name, mock):
			mock.return_value = 0.5
			print(random.random())
			with patch.object(random, 'random') as mock:
				mock.return_value = 0.4
				return getattr(self.wrapped, name)

	return Wrapper


@decorator
class C(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def print_rand(self):
    	print(random.random())


if __name__ == '__main__':
    c = C(1,2)
    #print(c.x)
    c.print_rand()

