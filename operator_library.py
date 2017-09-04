import datetime
import operator
import types


def transform_dict_values_to_string(d):
	td = {}
	for key in d.keys():
		value = d[key]
		td[key] = value
		if value is not None:
			if type(value) == datetime.datetime:
				td[key] = value.strftime('%Y-%m-%d')
			if value.__class__.__name__ == 'bool':
				td[key] = 'male' if operator.truth(value) else 'female'
	return td

def describe_person(d):
	td = transform_dict_values_to_string(d)

	generic_arg_list =  (td['first_name'], td['last_name'], td['gender'], td['date_of_birth'])
	generic_info = "%s %s is a %s born on %s" % generic_arg_list

	if operator.truth(td['college']):
		print(generic_info + (', and attended %s.' % td['college']))
	else:
		print(generic_info + '.')


john_doe_info = {
	'first_name': 'John',
	'last_name': 'Doe',
	'gender': True,
	'date_of_birth': datetime.datetime(year=1997, month=7, day=31),
	'college': 'American University',
}

jane_smith_info = {
	'first_name': 'Jane',
	'last_name': 'Smith',
	'gender': False,
	'date_of_birth': datetime.datetime(year=1998, month=8, day=30),
	'college': None,
}

if __name__ == '__main__':
	describe_person(john_doe_info)
	describe_person(jane_smith_info)

