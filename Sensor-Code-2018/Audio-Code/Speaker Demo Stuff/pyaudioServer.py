# pyaudio callback server

import pyaudio, time, socket
from constants import *
from audioplayer import *

player = AudioPlayer(CHUNK_SIZE, WIDTH, RATE, CHANNELS)

s = socket.socket()
s.bind(("",PORT))

s.listen(1)
client, address = s.accept()

print("Connection from: " + str(address))

while True:
    data = client.recv(8192)
    if not data:
        break
    
    #print("From connected user: " + data)
    player.audioData = data
    player.play()

client.close()
player.close()
