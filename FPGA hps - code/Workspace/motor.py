import os
import time
import gpio as gp
print(1)
gp.gpioUnexport(1803)
gp.gpioUnexport(1804)
gp.gpioUnexport(1805)
gp.gpioUnexport(1806)
print(2)
gp.gpioExport(1803)
gp.gpioExport(1804)
gp.gpioExport(1805)
gp.gpioExport(1806)
print(3)
gp.gpioDirection(1803,'out')
gp.gpioDirection(1804,'out')
gp.gpioDirection(1805,'out')
gp.gpioDirection(1806,'out')

print(4)

level = 650
while True:

    print(5)
            
    gp.gpioValue(1803,0)
    gp.gpioValue(1804,0)
    gp.gpioValue(1805,0)
    gp.gpioValue(1806,0)

    if (level>=0 and level<400):

    
        ##time.sleep(5)

        gp.gpioValue(1803,1)    #// watering the field
        gp.gpioValue(1804,0)

        gp.gpioValue(1805,0)
        gp.gpioValue(1806,0)
        print("M1 watering ")
    elif (level > 400 and level <500):
                                   # motors off in fields water field
        gp.gpioValue(1803,0)
        gp.gpioValue(1804,0)
        gp.gpioValue(1805,0)
        gp.gpioValue(1806,0)
        print("motors off")

    else:
        gp.gpioValue(1803,0)
        gp.gpioValue(1804,0)
        gp.gpioValue(1805,1)
        gp.gpioValue(1806,0)
        print("M2 evacuating water")

    time.sleep(5)

    print('rule breaked')
    gp.gpioValue(1803,0)
    gp.gpioValue(1804,0)
    gp.gpioValue(1805,0)
    gp.gpioValue(1806,0)

    gp.gpioUnexport(1803)
    gp.gpioUnexport(1804)

    gp.gpioUnexport(1805)
    gp.gpioUnexport(1806)
        
        




