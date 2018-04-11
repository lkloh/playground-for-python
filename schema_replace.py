from voluptuous import All, In, Schema

def replace_boolean(value):
  if value == 'boolean':
    return 'boolean_special'
  else:
    return value

validate_params = Schema({
  'gender': In(['male', 'female', 'other']),
  'type': All(In(['boolean', 'string', 'unicode']), replace_boolean),
}, required=True)

params1 = {
  'gender': 'female',
  'type': 'boolean',
}
params1 = validate_params(params1)
print params1
print '\n'


params2 = {
  'gender': 'female',
  'type': 'string',
}
params2 = validate_params(params2)
print params2
print '\n'


params3 = {
  'gender': 'male',
  'type': 'alien',
}
params3 = validate_params(params3)
print params3




