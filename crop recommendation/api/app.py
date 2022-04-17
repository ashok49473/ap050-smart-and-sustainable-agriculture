import pickle
from flask import Flask, request, jsonify, abort
import logging
import numpy as np
app = Flask(__name__)          
app.logger.setLevel(logging.DEBUG)
import warnings
warnings.filterwarnings('ignore')
import json
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

connect_str = "DefaultEndpointsProtocol=https;AccountName=datafromfpga;AccountKey=g1Z9bLD4RZZKKeLGoZYKGRFHxM7zlqmUscB5W40wdYg5PuL0sxX1GlxxrVJSdCNIQSs/qFasHY+mNDCuEG3XVQ==;EndpointSuffix=core.windows.net"
blob_service_client = BlobServiceClient.from_connection_string(connect_str)
with open('crop_recommendation_model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('encoder.pkl', 'rb') as f:
    encoder = pickle.load(f)

def class_predict(x):
    out = encoder.inverse_transform(model.predict(np.array(x).reshape(1, -1)))[0]
    return out

@app.route('/')
def home():
    return "Crop recommendation api Home"

@app.route("/plant/crop_recommendation", methods=['POST', 'GET'])
def test_method():
    if request.method == 'GET':
        return {"code":201}
    # print(request.json)     
    # if not request.json or 'data' not in request.json: 
    #     abort(400)
    data = request.json['data']
    print(data)
    keys = ['N', 'P', 'K', 'temperature', 'humidity', 'ph']

    x = [data[key] for key in keys]

    label = class_predict(x)

    return jsonify({"prediction": label})

container = "rfsdata"
container_client = blob_service_client.get_container_client(container=container)

@app.route("/rfs", methods = ['GET', 'POST'])
def send_rfs_to_blob():
    if request.method == "GET":
        return jsonify({"api_status":201})
    if request.method == "POST":

        rfs_data = request.json['rfs_data']
        with open('rfsdata.json', 'w') as f:
            json.dump(rfs_data, f)
        
        with open('rfsdata.json', 'rb') as jsondata:
            container_client.upload_blob(data=jsondata, name='rfsdata.json', overwrite=True)
            print("Success")
        return {"status":200}

    
def run_server_api():
    app.run(host="0.0.0.0")


if __name__ == "__main__":     
    run_server_api()


    

