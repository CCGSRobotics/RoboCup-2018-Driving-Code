from connect import *
import lib_threading1
from constants import *
        
def switch(state):
    if state == SWITCHON:
        sock.sendall(bytes("OFF\n", "utf-8"))
        return SWITCHOFF
    sock.sendall(bytes("ON\n", "utf-8"))
    return SWITCHON
