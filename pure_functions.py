
import datetime

class Person:
	def __init__(self, first, last, bday, is_male, college=None, college_major=None, grad_year=None):
		self.first_name = first_name
    	self.last_name = last_name
    	self.birthday = bday
    	self.is_male = is_male
    	self.college = college
    	self.college_major = major
    	self.grad_year = grad_year

	def update(params):
		for key, val in self.__dict__.iteritems():
			print key


john_doe = Person('John', 'Doe', True, datetime.datetime(1980, 07, 31))
jane_roe = Person(
	'Jane', 
	'Roe', 
	False, 
	datetime.datetime(1981, 9, 1), 
	{'college': 'Carnegie Mellon', 'department': 'Arts & Sciences'},
	2015
)
alice_anderson = Person(
	'Alice', 
	'Anderson', 
	False, 
	datetime.datetime(2002, 8, 28), 
	{'college': 'Stanford', 'department': 'School of Engineering'}
)


johns_new_college = {
	college: {
		'college': 'Harvard',
		'department': 'Arts & Sciences'
	},
	college_major: 'History',
	grad_year: '2014',
}

john_doe.update(johns_new_college)






