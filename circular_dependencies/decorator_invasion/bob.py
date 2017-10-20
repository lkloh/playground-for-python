
def bobby():
	return 'Bob'

def yolo():
	from alice import test
	test()
	return 'yolo'

if __name__ == '__main__':
	yolo()
