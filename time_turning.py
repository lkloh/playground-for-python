from freezegun import freeze_time
from datetime import datetime


def basic():
	obama_birthday = datetime(year=1961, month=8, day=4)
	freezer = freeze_time(obama_birthday)
	freezer.start()
	assert datetime.now() == obama_birthday

def move_forward_in_time():
	obama_birthday = datetime(year=1961, month=8, day=4)
	with freeze_time(obama_birthday) as frozen_datetime:
		print frozen_datetime()
		assert frozen_datetime() == obama_birthday


if __name__ == '__main__':
	basic()
	move_forward_in_time()

