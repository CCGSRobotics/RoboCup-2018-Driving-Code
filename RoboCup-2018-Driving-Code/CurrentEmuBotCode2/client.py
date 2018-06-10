#!/usr/bin/env python
import time
from controller import *
from constants import *
import WheelArmClass as WAC
import BasicClasses as BC
import os

Li = 0
Ri = 0
ForwardsI = 0

SwitchONN = True
alf = ""
backwardsl = 1
backwardsr = 1
FlippersModeL = 1
FlippersModeR = 1
RJoyStickPressed = 0
LJoyStickPressed = 0

Arm = WAC.Arm([5,6,7])
WheelL1 = BC.Wheel(1)
WheelR2 = BC.Wheel(2)
WheelL3 = BC.Wheel(3)
WheelR4 = BC.Wheel(4)

def LWheels(speed):
    if speed == 0:
        WheelL1.moveWheel(0)
        WheelL3.moveWheel(0)
    else:
        WheelL1.moveWheel(speed)
        WheelL3.moveWheel(speed)
def RWheels(speed):
    if speed == 0:
        WheelR2.moveWheel(0)
        WheelR4.moveWheel(0)
    else:
        WheelR2.moveWheel(speed)
        WheelR4.moveWheel(speed)
print("Vroom Vroom!")
for event in gamepad.read_loop():
    try:
        x = event.code
        y = event.value
        z = event.type
        if x != 0:
            if 0: print(event)
            
            elif x == LEFT_TRG:
                if Li == 3 or y <= 0:
                    if y > 0:
                        LWheels(y*4*backwardsl)
                    else:
                        LWheels(0)
                    Li = 1
                else:
                    Li = Li + 1
            elif x == RIGHT_TRG:
                if Ri == 3 or y <= 0:
                    if y > 0:
                        RWheels(-(y*4*backwardsr))
                    else:
                        RWheels(0)
                    Ri = 1
                else:
                    Ri = Ri + 1    
            elif x == LB:
                if y == 1:
                    if backwardsl > 0:
                        backwardsl = -1
                    else:
                        backwardsl = 1
            elif x == RB:
                if y == 1:
                    if backwardsr > 0:
                        backwardsr = -1
                    else:
                        backwardsr = 1
                        
            elif x == LHORIZ:
                if ForwardsI == 3 or y <= 0:
                    if y > 0:
                        LWheels(y/40)
                        RWheels(y/40)
                    elif y < 0:
                        LWheels(y/40)
                        RWheels(y/40)
                    
                    else:
                        LWheels(0)
                        RWheels(0)
                    ForwardsI = 1
                else:
                    ForwardsI = ForwardsI + 1
            elif x == LVERT:
                LWheels(-(y/40))
                RWheels((y/40))


                
            elif x == DPadHoriz:
                if y == 1:
                    Arm.MovePan(direction='increase')
                    #Pan forward
                elif y == -1:
                    Arm.MovePan(direction='decrease')
                    #Pan backward
                elif y == 0:
                    Arm.MovePan(direction='neutral')
                    #Stop Pan moving                                       
            elif x == DPadVert:
                if y == -1:
                    Arm.MoveTilt(direction='increase')
                    #Tilt forward
                elif y == 1:
                    Arm.MoveTilt(direction='decrease')
                    #Tilt backward
                elif y == 0:
                    Arm.MoveTilt(direction='neutral')
                    #Stop tilt moving
            elif x == Y:
                if y == 1:
                    Arm.MoveShoulder(direction='increase')
                    #Shoulder moving forward
                elif y == 0:
                    Arm.MoveShoulder(direction='neutral')
              #Stop Shoulder Moving
            elif x == A:
                if y == 1:
                    Arm.MoveShoulder(direction='decrease')
                    #shoulder moving back
                elif y == 0:
                    Arm.MoveShoulder(direction='neutral')
                    #Stop Shoulder Moving
                    
            elif x == X:
                Arm.MoveArmSetPos(ShoulderPos=512,TiltPos=200,PanPos=512)

            elif x == B:
                if SwitchONN and y != 0:
                    SwitchOFF()
                    SwitchONN = False
                    print("OFF")
                elif y != 0:
                    SwitchON()
                    SwitchONN = True
                    print("ON")
            elif x == START:
                #Arm.MoveArmSetPos(ShoulderPos=200,TiltPos=200,PanPos=512)
                Arm.reset()
                WheelL1.moveWheel(0)
                WheelL3.moveWheel(0)
                WheelR2.moveWheel(0)
                WheelR4.moveWheel(0)
                #Turn servos off
                #wait 0.5 seconds
                #Turn servos on
                #Wait 0.5 seconds
                #Reset all servos to original positions
            elif x == BACK:
                WheelL1.moveWheel(0)
                WheelL3.moveWheel(0)
                WheelR2.moveWheel(0)
                WheelR4.moveWheel(0)
                #Robot in arm front position
                #Arm.MoveArmSetPos(ShoulderPos=512,TiltPos=200,PanPos=512)
            else:
                print(event, 'none')
    except BrokenPipeError as e:
        print(e)

thread1.direction = ""
