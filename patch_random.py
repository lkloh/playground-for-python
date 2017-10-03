# Dependencies: Python 3

import random
from unittest.mock import patch

@patch.object(random, 'random')
def get_random_float_patch_object(test_random):
	test_random.return_value = 0.7
	print(random.random())

@patch('random.random')
def get_random_float_patch(mock_random):
	mock_random.return_value = 0.5
	print(random.random())

if __name__ == '__main__':
	# get_random_float_patch()
	get_random_float_patch_object()
