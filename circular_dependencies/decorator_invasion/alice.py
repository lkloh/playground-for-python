from bob import bobby, yolo
from decorator_impl import decorator

@decorator
def wonderland():
	yolo()
	test()
	return bobby() + ' loves Alice'

def test():
	print 'I am a test'

if __name__ == '__main__':
	print wonderland()
