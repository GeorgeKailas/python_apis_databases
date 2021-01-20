'''
Building on the previous example, create a list of all of the emails of the users and print
the list to the console.

'''

import requests
from pprint import pprint

base_url = "http://demo.codingnomads.co:8080/tasks_api/users"
response = requests.get(base_url)

data = response.json()
# inner_data = data['data']
email_list = []
# filt_key = ['email']
# email_list = list(map(inner_data.get, filt_key))
# print(email_list)
# pprint(email)
# print(len(inner_data))
# pprint(inner_data[:5])
for i in data['data']:
   email_list.append(i['email'])
print(email_list)

# print(data['data'][0]['email'])
