import string
import json
import requests
import os
import random



chars = string.ascii_letters + string.digits + '!#$%&*'
random.seed = (os.urandom(1024))
url = 'htttp://INSERT YOUR URL HERE' #Insert the URL / Network endpoint that you are trying to send the spam to

names = json.loads(open('name.json').read())

for name in names:
	randomizeEnd = ''.join(random.choice(string.digits))
	userSend = name.lower() + randomizeEnd + '@gmail.com'
	passSend = ''.join(random.choice(chars) for i in range(6))

	requests.post(url, allow_redirects=False, data={
			'username': userSend,
			'password': passSend
	})

	print('sending username: %s and password: %s' % (userSend, passSend))

print("Sending complete.")