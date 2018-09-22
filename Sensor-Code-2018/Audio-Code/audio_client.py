"""A pyaudio callback client"""

import socket
import time
import constants
import pyaudio

def callback(client, in_data, frame_count, time_info, status):
    """A callback function for the pyaudio.PyAudio audio stream"""
    client.send(in_data)
    return in_data, pyaudio.paContinue

def main():
    """audio_server.py: main function"""
    audio = pyaudio.PyAudio()
    socket_client = socket.socket()
    socket_client.connect((constants.HOST, constants.PORT))

    stream = audio.open(
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

    audio.terminate()
    socket_client.close()

main()
