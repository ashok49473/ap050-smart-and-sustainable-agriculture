import io
import json                    
import base64                  
import logging             
import numpy as np
from PIL import Image
from flask import Flask, request, jsonify, abort
import os
from utils import predict
from tensorflow.keras.preprocessing.image import load_img, img_to_array
os.environ["CUDA_VISIBLE_DEVICES"]="-1"
#############################################################################
app = Flask(__name__) 
app.logger.setLevel(logging.DEBUG)

@app.route('/')
def home():
    return "Home"


@app.route("/plant/disease_prediction", methods=['POST'])
def test_method():             
    if not request.json or 'image' not in request.json: 
        abort(400)
    im_b64 = request.json['image']
    img_bytes = base64.b64decode(im_b64.encode('utf-8'))
    img = Image.open(io.BytesIO(img_bytes)).save('uploads/do.png')
    img = img_to_array(load_img('uploads/do.png', target_size=(128, 128)))
    img = np.expand_dims(img, 0)


    plant_name = request.json['plant_name']
    result_dict = predict(plant_name, img)
    return jsonify(result_dict)

def run_server_api():
    app.run(debug=True)
  
if __name__ == "__main__":     
    run_server_api()