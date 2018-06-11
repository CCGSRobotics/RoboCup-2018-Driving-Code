from py_read_serial import *
import sys
import time
import os

'''
Put all the sensor names in this list here, and plug them in accordingly.
Make sure they are plugged in correctly, otherwise your data will be wrong.
'''

messages = {
    0: ["The CO2 Content of the surrounding environment is", "ppm (parts per million)."],
    1: ["The current temperature is", "*C."]
}
numOfSensors = len(messages)
os.system('clear')
while 1:
    for x in range(numOfSensors  ):
        while 1:
            try:
                sensor = readPins() # sensor = {'num': sensorID, 'value': some number}
                break
            except:
                pass
        if sensor['num'] == 1:
            sensor['value'] = round((57*(sensor['value']-20))/100,1)
        print(messages[sensor['num']][0], sensor['value'], messages[sensor['num']][1])
    time.sleep(0.5)
    os.system('clear')
