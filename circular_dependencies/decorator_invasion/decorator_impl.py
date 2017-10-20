
def decorator(func):
	def wrapper():
		print 'Hi I am a decorator'
		return func()
	return wrapper
