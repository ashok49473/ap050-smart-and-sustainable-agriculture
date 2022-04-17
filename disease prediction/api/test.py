import base64
import json                    
import requests

api = 'https://disease-prediction-api.azurewebsites.net/plant/disease_prediction'
image_file = 'test2.jpg'

with open(image_file, "rb") as f:
    im_bytes = f.read()        
im_b64 = base64.b64encode(im_bytes).decode("utf8")

headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
  
payload = json.dumps({"image": im_b64, "plant_name": "rice"})
response = requests.post(api, data=payload, headers=headers)

try:
    data = response.json()     
    print(data)                
except requests.exceptions.RequestException:
    print(response.text)
