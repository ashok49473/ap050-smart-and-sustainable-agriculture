import os
import time
#print("vasu")

def gpioExport(pin):
    os.system('echo %d > /sys/class/gpio/export'%(pin))
def gpioUnexport(pin):
    os.system('echo %d > /sys/class/gpio/unexport'%(pin))
def gpioDirection(pin,direc):
    os.system('echo %s > /sys/class/gpio/gpio%d/direction'%(direc,pin))
def gpioValue(pin,val):
    os.system('echo %d > /sys/class/gpio/gpio%d/value'%(val, pin))
#print("ashok")
