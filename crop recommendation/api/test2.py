import requests
import json

api = r'https://crop-recommendation.azurewebsites.net/rfs'
data = {
    "rfs_data": {
        "temperature":31,
        "humidity":10
        }
    }

headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
  
payload = json.dumps(data)
response = requests.post(api, data=payload, headers=headers)
try:
    data = response.json()     
    print(data)                
except requests.exceptions.RequestException:
    print(response.text)
