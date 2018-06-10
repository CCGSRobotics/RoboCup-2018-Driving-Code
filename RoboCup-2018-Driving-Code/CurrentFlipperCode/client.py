#!/usr/bin/env python
import time
from controller import *
from constants import *
import WheelArmClass as WAC
import sys

Li = 0
Ri = 0
ForwardsI = 0

SwitchONN = True
alf = ""
backwardsl = 1
backwardsr = 1
RJoyStickPressed = 0
LJoyStickPressed = 0

Arm = WAC.Arm([9,10,11])
BRFlipper = WAC.Flipper(1,5)
BLFlipper = WAC.Flipper(2,6)
FRFlipper = WAC.Flipper(3,7)
FLFlipper = WAC.Flipper(4,8)

def LWheels(speed):
    if speed == 0:
        FLFlipper.MoveWheel('none',0)
        BLFlipper.MoveWheel('none',0)
    else:
        FLFlipper.MoveWheel('Forwards',speed)
        BLFlipper.MoveWheel('Forwards',speed)
def RWheels(speed):
    if speed == 0:
        FRFlipper.MoveWheel('none',0)
        BRFlipper.MoveWheel('none',0)
    else:
        FRFlipper.MoveWheel('Forwards',speed)
        BRFlipper.MoveWheel('Forwards',speed)

print("Vroom Vroom!")
sys.stdout.flush()
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
            elif x == RCLICK:
                RJoyStickPressed = y
            elif x == LCLICK:
                LJoyStickPressed = y
            elif x == LVERT:
                if LJoyStickPressed:
                    if y > 7000:
                        BLFlipper.MoveFlipper('decrease')
                        #Move Left Back flipperup
                    elif y < -7000:
                        BLFlipper.MoveFlipper('increase')
                        #Move Left Back Flipper Down
                    else:
                        BLFlipper.MoveFlipper('neutral')
                else:
                    if y > 7000:
                        FLFlipper.MoveFlipper('increase')
                        #Move Left Front flipperup
                    elif y < -7000:
                        FLFlipper.MoveFlipper('decrease')
                        #Move Left Front Flipper Down
                    else:
                        FLFlipper.MoveFlipper('neutral')
                        BLFlipper.MoveFlipper('neutral')
            elif x == RVERT:
                if RJoyStickPressed:
                    if y > 7000:
                        BRFlipper.MoveFlipper('increase')
                        #Move Right Back flipperup
                    elif y < -7000:
                        BRFlipper.MoveFlipper('decrease')
                        #Move Right Back Flipper Down
                    else:
                        BRFlipper.MoveFlipper('neutral')                        
                else:
                    if y > 7000:
                        FRFlipper.MoveFlipper('decrease')
                        #Move Right Front flipperup
                    elif y < -7000:
                        FRFlipper.MoveFlipper('increase')
                        #Move Right Front Flipper Down
                    else:
                        FRFlipper.MoveFlipper('neutral')
                        BRFlipper.MoveFlipper('neutral')  
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
            elif x == X:
                Arm.MoveArmSetPos(ShoulderPos=512,TiltPos=200,PanPos=512)
                #Arm straight up loking down
            elif x == BACK:
                #Arm.MoveArmSetPos(ShoulderPos=200,TiltPos=200,PanPos=512)
                FLFlipper.MoveWheel('none',0)
                FRFlipper.MoveWheel('none',0)
                BLFlipper.MoveWheel('none',0)
                BRFlipper.MoveWheel('none',0)
                backwardsl = 1
                backwardsr = 1
                #Turn servos off
                #wait 0.5 seconds
                #Turn servos on
                #Wait 0.5 seconds
                #Reset all servos to original positions
            elif x == START:
                Arm.reset()
                BRFlipper.reset()
                BLFlipper.reset()
                FRFlipper.reset()
                FLFlipper.reset()
                backwardsl = 1
                backwardsr = 1
                #Arm.MoveArmSetPos(ShoulderPos=200,TiltPos=200,PanPos=512)
                #Robot in arm front position
            elif x == B:
                print('sdfhjkkhjgkghkjdfjkh')
                pass
                #turn servos on and off
            else:
                #print(event, 'none')
                pass
    except BrokenPipeError as e:
        print(e)

thread1.direction = ""
