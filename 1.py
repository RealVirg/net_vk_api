import requests
import json
print('enter the id of the user whose friend list you want to view')
id = input()
response = requests.get('https://api.vk.com/method/friends.get?user_id=' + id + '&v=5.52&access_token=407cb444407cb444407cb444ed400dac554407c407cb4441eea641cd8e0e63dd5e8d458')
json_1 = json.loads(response.content)
for obj in json_1:
	if obj == 'response':
		for item in json_1['response']:
			if item == "items":
				for people in json_1['response']['items']:
					people = requests.get('https://api.vk.com/method/users.get?user_id=' + str(people) +
						'&v=5.52&access_token=407cb444407cb444407cb444ed400dac554407c407cb4441eea641cd8e0e63dd5e8d458')
					json_2 = json.loads(people.content)
					firstname = ""
					lastname = ""
					for o in json_2:
						if o == 'response':
							for info in json_2['response']:
								firstname = info['first_name']
								lastname = info['last_name']
					print(firstname, lastname, sep=" ")
