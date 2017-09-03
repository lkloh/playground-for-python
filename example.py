from datetime import datetime
import operator


def describe_person(person_dict):
	generic_arg_list =  (person_dict['first_name'], person_dict['last_name'], person_dict['gender'], person_dict['date_of_birth'])
	generic_info = "%s %s is a %s born on %s." % generic_arg_list
	if operator.truth(person_dict['college']):
		print generic_info + (' He went to %s.' % person_dict['college'])
	else:
		print generic_info


john_doe_info = {
	'first_name': 'John',
	'last_name': 'Doe',
	'gender': 'male',
	'date_of_birth': datetime(year=1997, month=7, day=31).strftime('%Y-%m-%d'),
	'college': 'American University',
}

tom_smith_info = {
	'first_name': 'Tom',
	'last_name': 'Smith',
	'gender': 'male',
	'date_of_birth': datetime(year=1998, month=8, day=30).strftime('%Y-%m-%d'),
	'college': None
}

describe_person(john_doe_info)
describe_person(tom_smith_info)

