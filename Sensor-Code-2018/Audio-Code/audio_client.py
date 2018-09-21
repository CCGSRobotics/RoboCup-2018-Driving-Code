import constants
import pyaudio
from socket import socket
from time import sleep

audioClient = pyaudio.PyAudio()
socketClient = socket()
socketClient.connect((constants.HOST, constants.PORT))

def callback(in_data, frame_count, time_info, status):
    global socketClient
    socketClient.send(in_data)
    return in_data, pyaudio.paContinue

stream = audioClient.open(
    format=constants.WIDTH,
    channels=constants.CHANNELS,
    rate=constants.RATE,
    input=True,
    output=False,
    stream_callback=callback
)

stream.start_stream()
while stream.is_active():
    time.sleep(0.1)

stream.stop_stream()
stream.close()

audioClient.terminate()
socketClient.close()
