
import json
import requests


STATUS_OK = 200

def is_hirable(contributor):
	username = contributor.get('login')
	response = requests.get("https://api.github.com/user/" + username)
	if response.status_code == STATUS_OK:
		return contributor.get('hirable') or contributor.get('followers')

def get_hirable_contributors():
	response = requests.get("https://api.github.com/repos/django/django/contributors")
	if response.status_code == STATUS_OK:
		contributors = json.loads(response.content)
		return [contributor['login'] for contributor in contributors if is_hirable(contributor)]

print get_hirable_contributors()










