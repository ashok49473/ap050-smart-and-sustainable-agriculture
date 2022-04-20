
# Final Paper:
http://www.innovatefpga.com/cgi-bin/innovate/teams.pl?Id=AP050&All=1

# Youtube Video Link:
https://youtu.be/y86IUrFhL6M

High Level Block diagram:
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
![image](https://user-images.githubusercontent.com/73692009/164240193-50192221-3b05-44f8-9183-4f819f8740c6.png)


We need instantaneous processing for all the inputs. Also, we require a high computing power device. That can be done with the DE-10 Nano kit. Therefore, FPGA is the best choice for the development of our device.
