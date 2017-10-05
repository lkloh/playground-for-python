

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

		def __getattr__(self, name):
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

