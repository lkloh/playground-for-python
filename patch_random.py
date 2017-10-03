# Dependencies: Python 3

import random
from unittest.mock import patch

@patch.object(random, 'random')
def get_random_float(test_random):
	test_random.return_value = 0.5
	print(random.random())

if __name__ == '__main__':
	get_random_float()