
import sys
import logging
import traceback

def sys_exc_info_experiment():
	print '\nsys_exc_info_experiment'
	try:
	    1/0
	except:
	    exc_type, exc_value, exc_traceback = sys.exc_info()
	    print exc_type
	    print exc_value
	    print str(exc_traceback)
	finally:
		print '\n'

def traceback_experiment():
	print '\nsys_exc_info_experiment'
	try:
	    1/0
	except Exception as err:
	   traceback.print_exc()
	finally:
		print '\n'

if __name__ == '__main__':
	sys_exc_info_experiment()
	traceback_experiment()