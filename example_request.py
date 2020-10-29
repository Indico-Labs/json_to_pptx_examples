import requests

token = "<YOUR_TOKEN>"
data_path = "example_data/bar.json"

# preparing body for request
with open(data_path, 'rb') as f:
    body = f.read()

url = 'https://api.pptxbuilder.com/api/v1/convert'
headers = {"content-type": "application/json"}
headers['Authorization'] = 'Bearer ' + token


response = requests.post(url, data=body, headers=headers)
content = response.content

if response.status_code != 200:
    print(response.json())
else:
    disposition = response.headers['Content-Disposition']
    file_name = disposition.split(';')[-1].strip().split('=')[1]
    with open("exports/"+str(file_name), 'wb') as w:
        w.write(content)