from voluptuous import In, Schema

def replace_boolean(value):
  if value == 'boolean':
    return 'boolean_special'
  else:
    return value

validate_params = Schema({
  'gender': In(['male', 'female', 'other']),
  'type': replace_boolean,
}, required=True)

params = {
  'gender': 'female',
  'type': 'boolean',
}
params = validate_params(params)
print params




