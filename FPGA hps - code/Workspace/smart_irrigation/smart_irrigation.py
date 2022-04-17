import serial
import time
import json
import os
import gpio as gp
import datetime


gp.gpioUnexport(1803)
gp.gpioUnexport(1804)
gp.gpioUnexport(1805)
gp.gpioUnexport(1806)
#print(2)
gp.gpioExport(1803)
gp.gpioExport(1804)
gp.gpioExport(1805)
gp.gpioExport(1806)
#print(3)
gp.gpioDirection(1803,'out')
gp.gpioDirection(1804,'out')
gp.gpioDirection(1805,'out')
gp.gpioDirection(1806,'out')

start_date = datetime.datetime(2022, 3, 15)   #crop starting date 
while True:
    try:
    
        serialport = serial.Serial('/dev/ttyACM0',baudrate=9600,timeout=3) #here we collected sensor data from Arduino Uno board using Serial Communication
        arduinodata = serialport.readline()

        x=str(arduinodata.decode()).replace('\r\n', '').split("::")
        #print(x)
        #arduino code sentence  Serial.println((String)"Temp:"+temperature+"::EC:"+ec+"::pH:"+ph_act+"::Nitro:"+val1+"::Potas:"+val2+"::Phosp:"+val3+"::level:"+level+"::Moist:"+soilMoistureValue);"""
        
        if x != [''] and len(x)==8:
            dict_ = {ele.split(':')[0]:ele.split(':')[1] for ele in x}
        else:
            dict_ = 0
            
        print(dict_)
        time.sleep(3)
        if dict_ :
            level = int(dict_['level'])
            print("water level :",level) 
            with open('new.json','w') as f:
                json.dump(dict_, f)
            
            ## smart irrigation
            temp = datetime.datetime.now() - start_date
            days = temp.days
            
            # Stage 1:
            if 0 <= days <= 25:
                in_min, in_max = 0, 510
                off_min, off_max = 510, 550
                out_max = 550

            # Stage 2:
            if 25 <= days <= 27:
                in_min, in_max = 0, 380
                off_min, off_max = 380, 410
                out_max = 410
                
            # Stage 3:
            if 28 <= days <= 29:
                in_min, in_max = 0, 570
                off_min, off_max = 570, 580
                out_max = 580

             # Stage 4:
            if 29 <= days <=105:
               in_min, in_max = 0, 570
               off_min, off_max = 570, 580
               out_max = 580
                 

            # Irrigation
            if (level>in_min and level<in_max):
                gp.gpioValue(1803,1)    #// watering the field
                gp.gpioValue(1804,0)
                gp.gpioValue(1805,0)
                gp.gpioValue(1806,0)
                print("\n")
                print("Watering into feild")
                print("\n")
                print("INLET Motor is ON and OUTLET Motor is OFF")
                
            elif (level > off_min and level<off_max):
                gp.gpioValue(1805,0)    # stagnate - off mode
                gp.gpioValue(1806,0)
                gp.gpioValue(1803,0)
                gp.gpioValue(1804,0)
                print("\n")
                print("Water Stagnate")
                print("\n")
                print("INLET and OUTLET Motors remains OFF")
        
            elif level > out_max:
                gp.gpioValue(1803,0)   #removing excess water from feild
                gp.gpioValue(1804,0)
                gp.gpioValue(1805,1)
                gp.gpioValue(1806,0)
                print("\n")
                print("Evacuating Excess water from feild")
                print("\n")
                print("OUTLET Motor ON and INLET Motor is OFF")

            else:
                print("Problem in watering ")
    except KeyboardInterrupt as e:

        print('rule breaked')
        gp.gpioValue(1803,0)
        gp.gpioValue(1804,0)
        gp.gpioValue(1805,0)
        gp.gpioValue(1806,0)

        gp.gpioUnexport(1803)
        gp.gpioUnexport(1804)

        gp.gpioUnexport(1805)
        gp.gpioUnexport(1806)

        
 

