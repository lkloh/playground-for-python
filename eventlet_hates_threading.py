import eventlet
eventlet.monkey_patch(os=True, select=True, socket=True, time=True)

from eventlet.greenpool import GreenPool, GreenPile
import math
import threading

def do_large_computation():
	s = 0
	for i in range(1000000):
		s += math.sqrt(i*i + 1)
	return s

def use_eventlet():
	pool = GreenPool(100)
	pile = GreenPile(pool)
	for i in range(10):
		pile.spawn(do_large_computation)
	return pile.next()

def use_threads():
	threads = []
	for i in range(10):
	    t = threading.Thread(target=do_large_computation)
	    threads.append(t)
	    t.start()

if __name__ == '__main__':
	use_threads()
	use_eventlet()