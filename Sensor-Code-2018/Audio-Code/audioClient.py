# Pyaudio callback client

import pyaudio, time, socket
from constants import *

def callback(in_data,frame_count,time_info,status):
    s.send(in_data)
    return in_data,pyaudio.paContinue

p = pyaudio.PyAudio()
s = socket.socket()
s.connect((HOST,PORT))

stream = p.open(
    format = WIDTH,
    channels = CHANNELS,
    rate = RATE,
    input = True,
    output = False,
    stream_callback = callback
)

stream.start_stream()
while stream.is_active():
    time.sleep(0.1)

stream.stop_stream()
stream.close()

s.close()
p.terminate()
