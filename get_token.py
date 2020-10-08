import requests
import json

key = "<A_VALID_COMPANY_KEY>"
user = "<A_VALID_USER>"
passwd = "<A_VALID_PASS>"

url = 'https://api.pptxbuilder.com/api/auth/token'

body = json.dumps({'key': key})
headers = {'Content-Type': 'application/json'}

response = requests.post(url, data=body, headers=headers,
                        auth=(user, passwd))

if response.status_code != 200:
    response_msg = response.json()
    print(response_msg['error'])
else:
    token = response.headers['Authentication-Token']
    content = response.content
    print(content,"Token:"+str(token))