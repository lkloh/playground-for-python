import eventlet
eventlet.monkey_patch(os=True, select=True, socket=True, time=True)

from eventlet.greenpool import GreenPool, GreenPile
import math
import time
import threading

def do_large_computation():
	s = 0
	for i in range(10000):
		s += math.sqrt(i*i + 1)
	print s

def wait_forever():
	print 'wait_forever'
	while True:
		print 'hi'
		time.sleep(1)

def use_eventlet():
	pool = GreenPool(100)
	pile = GreenPile(pool)
	for i in range(10):
		pile.spawn(wait_forever)
	print pile.next()

def use_threads():
	threads = []
	for i in range(10):
	    t = threading.Thread(target=do_large_computation)
	    threads.append(t)
	    t.start()

if __name__ == '__main__':
	use_eventlet()
	use_threads()