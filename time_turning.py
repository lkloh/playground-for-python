# Dependency:sudo pip install freezetime

from freezegun import freeze_time
from datetime import datetime

def basic():
	obama_birthday = datetime(year=1961, month=8, day=4)
	freezer = freeze_time(obama_birthday)
	freezer.start()

	assert datetime.now() == obama_birthday

	freezer.stop()

def move_forward_in_time():
	obama_birthday = datetime(year=1961, month=8, day=4)
	election_day = datetime(year=2008, month=11, day=8)
	with freeze_time(obama_birthday) as frozen_datetime:
		assert datetime.now() == obama_birthday
		frozen_datetime.move_to(election_day)
		assert datetime.now() == election_day

def failed_test():
	obama_birthday = datetime(year=1961, month=8, day=4)
	print datetime.now()
	assert datetime.now() == obama_birthday

if __name__ == '__main__':
	basic()
	move_forward_in_time()
	failed_test()
