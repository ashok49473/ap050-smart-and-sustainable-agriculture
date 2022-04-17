#################### imports ########################
import numpy as np
import json
from tensorflow.keras.models import load_model
from tensorflow import expand_dims
f = open('fertilizers_final.json')
database = json.load(f)
f.close()

##################### variables ######################
class_names_dict = {
    'rice':['bacterial-blight', 'blast', 'brown-spot', 'tungro'],
    'potato':['early-blight', 'healthy', 'late-blight'],
    'tomato':['bacterial-spot', 'early-blight', 'healthy', 'late-blight', 'leaf-mold'],
    'bell-pepper':['bacterial-spot', 'healthy']
}

##################### functions ######################

def predict(plant, img):
    model = load_model(f'models/{plant}.h5')
    pred = np.argmax(model.predict(img)[0])
    disease = class_names_dict[plant][pred]

    res = database[plant][disease]
    res['disease'] = disease
    return res

###########




