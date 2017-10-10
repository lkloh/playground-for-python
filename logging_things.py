
import logging
logging.basicConfig(filename='loggin_things_log.txt',level=logging.DEBUG)

_log = logging.getLogger(__name__)

if __name__ == '__main__':
	_log.warning("The air in San Francisco today is terrible.")

