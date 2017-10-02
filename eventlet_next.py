import eventlet
eventlet.monkey_patch(os=True, select=True, socket=True, time=True)

import time


def return_immediately():
	return None

def wait_one_second():
	time.sleep(1)
	return "wait_one_second"


def test_next():
	pile = eventlet.GreenPile(10)
	pile.spawn(return_immediately)
	pile.spawn(wait_one_second)
	return [p for p in pile][1]

if __name__ == '__main__':
	print test_next()