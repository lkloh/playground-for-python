# Inspired by https://wiki.python.org/moin/Generators
import resource

def output_peak_memory_usage_of_function(func):
	def wrapper(*args, **kwargs):
		func(*args, **kwargs)
		mega_bytes_used = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1000000.0
		print 'Peak memory usage for function %s: %f Mb' % (func.__name__, mega_bytes_used)
	return wrapper

@output_peak_memory_usage_of_function
def calculate_sum_by_creating_list_in_memory(n):
	i = 0
	arr = []
	while i < n:
		arr += [i]
		i += 1
	return sum(arr)

@output_peak_memory_usage_of_function
def calculate_sum_by_creating_list_with_generator(n):	
	def list_generator(n):
		i = 0
		while i < n:
			yield i
			i += 1
	return sum(list_generator(n))

if __name__=='__main__':
	calculate_sum_by_creating_list_with_generator(1000000)
	calculate_sum_by_creating_list_in_memory(1000000)