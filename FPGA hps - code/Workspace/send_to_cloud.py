##from unicodedata import name
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
import os
import time
import cv2

connect_str = "DefaultEndpointsProtocol=https;AccountName=datafromfpga;AccountKey=g1Z9bLD4RZZKKeLGoZYKGRFHxM7zlqmUscB5W40wdYg5PuL0sxX1GlxxrVJSdCNIQSs/qFasHY+mNDCuEG3XVQ==;EndpointSuffix=core.windows.net"
blob_service_client = BlobServiceClient.from_connection_string(connect_str)

container1 = "image"
container2 = "sensordata"
container3 = "rfsdata"

container1_client = blob_service_client.get_container_client(container=container1)
container2_client = blob_service_client.get_container_client(container=container2)
container3_client = blob_service_client.get_container_client(container=container3)

vid = cv2.VideoCapture(0)

while True:
    ret, frame = vid.read()
    if not ret:
        print("failed to capture the image")
    else:
        cv2.imwrite(filename='artifacts/crop.jpg',img=frame)
    
    try:
        with open('artifacts/crop.jpg', 'rb') as image:
            container1_client.upload_blob(data=image, name='crop.jpg', overwrite=True)

        with open('artifacts/sensor.json', 'rb') as jsn:
            container2_client.upload_blob(data=jsn, name='sensor.json', overwrite=True)

        with open('artifacts/rfs.json', 'rb') as rjsn:
            container2_client.upload_blob(data=rjsn, name='rfs.json', overwrite=True)

            
        print("Successful")
        time.sleep(10)
        
    except KeyboardInterrupt:
        break
    except Exception as e:
        print(e)
        


    
    




















