import threading
import time

from connect import *

class Joint(threading.Thread):
    def __init__(self, ID, position):
        threading.Thread.__init__(self)
        self.direction = "neutral"
        self.id = ID
        self.position = position
        
        self.moveJoint(self.position, 900)
    def run(self):
        while self.direction != "":
            if self.direction == "decrease":
                if self.position > 200:
                    self.position -= 15
            elif self.direction == "increase":
                if self.position < 800:
                    self.position += 15
            if self.direction != "neutral":
                self.moveJoint(self.position,900)
            time.sleep(0.1)
            
    def moveJoint(self, position, speed):

        #print(position)
        
        output = ''
        
        if self.id < 10:
            output += '0' + str(self.id)
        else:
            output += str(self.id)

        for i in range(4 - len(str(position))):
            output += '0'

        output += str(position)

        for i in range(4 - len(str(speed))):
            output += '0'

        output += str(position)

        output += '\n'
        #print(output)
        sock.sendall(bytes(output, 'utf-8')) 
   

class Wheel():
    def __init__(self, ID):
        self.id = str(ID)
        self.direction = "none"
        self.speed = 0
            
    def moveWheel(self, speed):
        self.speed = speed
        output = '0' + self.id

        if self.speed < 11 and self.speed > -11:
            self.speed = 0
        elif self.speed < 0:
            output += '-'
            self.speed = self.speed*-1

        for i in range(4 - len(str(self.speed))):
            output += '0'

        output += str(self.speed)
        #print(output)
        sock.sendall(bytes(output+"\n", 'utf-8'))

class Switch():
    def __init__(self):
        self.on = True

    def ChangeStatus():
        if self.on:
            sock.sendall(bytes("OFF\n", "utf-8"))
            self.on = False
        else:
            sock.sendall(bytes("ON\n", "utf-8"))
            self.on = True
