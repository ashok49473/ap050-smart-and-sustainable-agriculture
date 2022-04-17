import requests
import json

api = r'https://crop-recommendation.azurewebsites.net/plant/crop_recommendation'
data = {
    "data": {
        'N': 67,
        'P': 6767,
        'K': 677, 
        'temperature': 30.31, 
        'humidity':42.27,
        'ph': 77
        }
    }
print(data)

headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
  
payload = json.dumps(data)
response = requests.post(api, data=payload, headers=headers)
print(response)
try:
    data = response.json()     
    print(data)                
except requests.exceptions.RequestException:
    print(response.text)


