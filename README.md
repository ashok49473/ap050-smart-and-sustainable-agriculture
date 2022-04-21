
## Final Paper:
http://www.innovatefpga.com/cgi-bin/innovate/teams.pl?Id=AP050&All=1

## Youtube Video Link:
https://youtu.be/y86IUrFhL6M

### High Level Block diagram:
https://www.innovatefpga.com/attachment/member/2021/AP050-3A9EFC34B15CB14E/image/Slide%2016_9%20-%201%20(1).png

![Slide 16_9 - 1 (1)](https://user-images.githubusercontent.com/73692009/163812147-015cf86e-6b51-4a36-b443-d8c2bdf3f9eb.png)


Complete code that is related to Board is in ---> https://github.com/ashok49473/ap050-smart-and-sustainable-agriculture/tree/main/FPGA%20hps%20-%20code

There after all the code i.e Smart Irrigation, rfs Data, Camera, gpio's and cloud sending python files are in Workspace.


# AP050-Smart and Sustainable Agriculture using FPGA

“Farm at ease” (Technology to farming):
To meet the growing population of the world, some serious reforms are required in the agricultural sector to ensure that our food system is ready to meet the upcoming challenges. This pushes us to shift from traditional/conservative agricultural practices to sustainable practices. Further, these sustainable practices are integrated with technological advancements, the major challenges of the agriculture/farming across the world can be resolved in an efficient and effective manner.
The following are some of the key challenges posed by the agricultural sector:
1. There is a considerable gap between the adoptions of technology in the agricultural sector when compared to the non-agricultural sectors especially in third world countries.
2. Mismanagement in crop planning without the proper analysis of soil.
3. Overutilization/underutilization of fertilizers.
4. Mismanagement in irrigation and thereby the water scarcity/wastage may occur.
5. Delay in identification of weeds/pests.
6. Unable to adopt the best practices of agriculture in the other regions.
Proposed solution:
To address above challenges, we are proposing for a design of a system (IOT based with Mobile/Web application development/Message alert system) which will aid the farmer in the following way:
1. Crop recommendation based on the soil condition, climate and water availability of that region.
2. Automatic irrigation system depending upon the crop requirement.
3. Recommendation of organic means of agriculture practice in place of fertilizers to the most possible extent.
4. Disease detection in crops using image processing.
5. Recommendation/alert system will be made in a simple manner and if possible, voice instructions will be given in regional languages.
Design idea:
The above-proposed idea will be designed initially as a real-time prototype device where FPGA board will be integrated with sensors such as NPK sensor, humidity sensor, temperature sensor, water level monitoring sensor, etc., Further, a communication shall be established between the FPGA board and mobile phone using FPGA virtues, Azure cloud, etc., This prototype device will be tested in a real-time agricultural field and based on the feedback/recommendations of the user (farmers) a robust system may be developed in future.

## SMART AND SUSTAINABLE AGRICULTURE USING FPGA
 

Growth in world population, increasing urbanization, and changing consumption habits means an increase in demand for food production and this must be achieved despite the challenges. To meet the food requirements of the growing population of the world, some serious reforms are required in the agricultural sector to ensure that our food system is ready to meet the upcoming challenges. This pushes us to shift from traditional/conservative agricultural practices to sustainable practices.

Further, these sustainable practices are integrated with technological advancements. The major challenges of agriculture/farming across the world can be resolved in an efficient and effective manner. The idea is to enable farmers more reliable monitoring their fields remotely, allowing the operation of several facilities at one time

Farmers don't need to repeat the same crop cultivation always instead, they can choose the crop as per their farm soil nature/condition. Farmers no longer have to apply water, fertilizers, and pesticides excess across their fields. Instead, they can use the minimum quantities required and target very specific areas, or even treat individual plants differently.

## DESIGN IDEA:

The above-proposed idea will be designed initially as a real-time prototype device only for paddy crop, where FPGA board will be integrated with sensors such as NPK sensor, pH sensor, EC sensor, Moisture sensor,  humidity sensor, temperature sensor, water level monitoring sensor, camera sensor, etc., Further, a communication shall be established between the FPGA board and mobile phone using FPGA virtues, Azure cloud, etc., This prototype device will be tested in a real-time agricultural field and based on the feedback/recommendations of the user (farmers) a robust system may be developed in future.

Our model workflow goes in 3 stages.

### 1. DATA READING

This Data reading is a two-step process.

Initial sensor data is used to perform soil testing and crop recommendation, here we collect data from NPK sensor, pH sensor, EC sensor, etc.

 Secondary sensor data is collected from sensors such as from NPK sensor, pH sensor, EC sensor, Moisture sensor, humidity sensor, temperature sensor, water level monitoring sensor, camera module, etc., is used for nutrient management (fertilizer recommendation), automatic irrigation and crop monitoring (including Weed detection). And this data is taken continuously throughout the crop from the field.

Further, all this sensor data is passed to the FPGA board.

### 2 DATA PROCESSING AND DECISION MAKING

We fix threshold values (for Paddy crop) from the Research data collected, this data is stored and further used to compare with real-time sensor data (Input data) in FPGA DE Nano-10 / Intel Azure Cloud.

After data processing, the system makes decisions in crop recommendation, fertilizer recommendation, automatic irrigation, weed detection, and pests/disease identification (when the farmer uploads a picture of the affected part of paddy).

### 3 CONTROLLING and OUTPUT DISPLAYING

As per decisions made by our system; it controls the irrigation system automatically. All the commands and results will be displayed in the Mobile/ Web application. Our system will guide and assist farmers through voice commands (Region language).  Farmer can able to monitor crop(plant growth) by receiving crop pictures regularly.

 

FPGA is used as a large computational data processing platform, and the time-consuming part of the image processing algorithm is transplanted into the FPGA.

FPGA can parallelize the tasks while the size consumption of such a system is less than the consumption of CPU and GPU. Especially for the image processing techniques, FPGA takes less time as compared with a microcontroller because of high-speed memory.

### Block Diagram

![image](https://user-images.githubusercontent.com/73692009/164343226-d338126b-543c-45b9-a061-3cfa1d51aeba.png)


We need instantaneous processing for all the inputs. Also, we require a high computing power device. That can be done with the DE-10 Nano kit. Therefore, FPGA is the best choice for the development of our device.

##### The functional description and implementation of the entire project is illustrated with the help of a flow chart as follows:
![image](https://user-images.githubusercontent.com/73692009/164343540-eecb01e3-1f5e-47fd-a266-029585752c48.png)


###### A. Functional description of the project:

The following are the various functions involved in the project: 

1.Sensor data collection

2.Crop recommendation system

3.Weed Detection

4.Disease Prediction

5.Smart Irrigation

6.Fertilizer recommendation

7.Overall crop monitoring system

Detailed description of above functions:

### 1.Sensor data collection:

Sensor data collection takes place in two parts.

Part 1: Data collection through serial communication from Arduino to DE-10Nano. All the analog sensors i.e. NPK Sensor, pH Sensor, Water level sensor, Soil Moisture sensor, Electric Conductivity Sensor and Soil Temperature sensor are connected to the Arduino Uno Microcontroller and read the data from them. This Arduino board is connected to DE-10Nano board using USB hub to OTG (USB-II mini) This sensor data is transferred through Serial Communication to FPGA Board. This Data will be sent to Azure Cloud for every 10 minutes and stored in Azure Containers.

Part 2:  Data collection from Temperature and Humidity sensors which are on RFS Daughter card is transferred to Azure IoT HUB as messages this data is being redirected to Azure Blob Storage.

All the data stored in Azure Cloud is being processed and displayed on Website.

Hardware Integration of the project:

![image](https://user-images.githubusercontent.com/73692009/164343498-86afa3a7-10f1-4da1-9371-48381ad67762.png)

Sensors we used in our project:

![image](https://user-images.githubusercontent.com/73692009/164343515-6d5e432e-7dd3-4de7-9df8-daf2004b9cf7.png)

## Implementation:

     1. Data collection through sensors:

Data collection through sensors is done with microcontroller (Arduino) and RFS Daughter Card. We collected the Analog sensor data from NPK Sensor, pH Sensor, Water level Sensor, Soil Moisture Sensor, Electric Conductivity Sensor and Soil temperature Sensor through Serial Communication to DE-10 Nano. We collected Temperature and Humidity data from Humidity sensor and Temperature Sensor presented in the RFS Daughter Card.

    2 .Integration of sensors data with DE-10 Nano:

Temperature sensor and Humidity Sensors present in RFS Daughter Card are connected to DE-10 Nan0 ( 2X20 GPIO 0 (JP1) pins).

NPK Sensor is connected to Arduino through  MAX 485 module, PH sensor and EC sensor is connected to arduino through BNC Probes. Likewise water level , soil moisture and soil temperature is connected to ArduinoUno; is connected to DE10-Nano board using USB Hub.

### 2.Crop recommendation system:

For Crop recommendation the sensor values from NPK, EC, and PH are taken as inputs. These parameters are observed previously and then it is stored in the database. The received data sets of soil and climatic conditions have applied to the machine learning algorithm. The support vector machine and linear regression are sensitive learning models. We have modelled four different learning algorithms, such as linear regression, decision tree, k-nearest neighbors, and XGBoost. In this study, we have chosen XGBoost for its better performance. We trained a Tree based ML model (XGBoost) to predict the recommended crop using features like NPK, PH, EC. The dataset was collected from Kaggle(Publicly available dataset).The algorithm checks the original data of the soil (DSoil) with the test data of the soil (DTest) and estimates the crop suitable for that area. a. Moreover the algorithm checks the humidity, temperature, and water level present in the field. The agricultural field is monitored by picturing the field once in a day using a digital camera. Achieved 95% accuracy on test data.

Implementation of Crop Recommendation.

![image](https://user-images.githubusercontent.com/73692009/164343711-d4ee16d2-60b2-46ea-9b9d-25718c6a09a9.png)

Sample Crop Data:

![image](https://user-images.githubusercontent.com/73692009/164343913-14cfb9fb-d901-48eb-8f5e-347b6962b460.png)

Confusion Matrix:

![image](https://user-images.githubusercontent.com/73692009/164343950-e89fa645-06be-45a8-b935-8023977eeec6.png)

Crop Resutls:

![image](https://user-images.githubusercontent.com/73692009/164343978-27c6b221-d5cd-4c12-a8b7-4d7dbf9206c9.png)

#### Our website recommending crop to the user :

![image](https://user-images.githubusercontent.com/73692009/164344089-5da4e4c4-46cd-4a82-bb2d-d88aa525ae4f.png)



7.Azure cloud/Website functionality:

* We collected input from various sensors using DE_10 NANO and for serial communication we have used Arduino.

* The collected data is then redirected to AZURE IOT HUB as messages using AZURE IOT client for the inference.

* The collected data from FPGA like sensor data, RFS data and daily crop image is sent to AZURE STORAGE ACCOUNT.

* We have developed a custom YOLOV5 model on AZURE APP SERVICE which receives a crop image from FPGA and sends the image with bounding boxes if any weed exists.

* The data stored in AZURE STORAGE ACCOUNT is simultaneously redirected to the web server to display the data on website.

* We have displayed XG-BOOST model for crop recommendation and CNN model for Disease Prediction as APIs using AZURE CONTAINERS in APP SERVICE.

* Farmer will interact with these APIs through website and the expected results like recommended crop and disease cure control are displayed to farmer in the website.

Azure Cloud/Website implementation:

![image](https://user-images.githubusercontent.com/73692009/164345483-69b7e8a8-7654-473b-86e4-f32ddabda118.png)

