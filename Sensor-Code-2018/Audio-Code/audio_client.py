"""A pyaudio callback client"""

import socket
import time
import constants
import pyaudio

AUDIO = pyaudio.PyAudio()
SOCKET_CLIENT = socket.socket()
SOCKET_CLIENT.connect((constants.HOST, constants.PORT))

def callback(in_data, frame_count, time_info, status):
    """A callback function for the pyaudio.PyAudio audio stream"""
    SOCKET_CLIENT.send(in_data)
    return in_data, pyaudio.paContinue

def main():
    """audio_client.py: main function"""

    stream = AUDIO.open(
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

    AUDIO.terminate()
    SOCKET_CLIENT.close()

main()
