import requests
import json

url = '<CUSTOM-VISON-END-POINT>'
payload = {"Url": "<IMAGE-URL>"}
headers = {'Prediction-Key': '<CHANGE-YOUR-CODE>','content-type': 'application/json'}

r = requests.post(url, data=json.dumps(payload), headers=headers)
print (r.text)