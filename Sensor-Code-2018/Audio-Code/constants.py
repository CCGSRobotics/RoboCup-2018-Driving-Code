"""Contains TCP Constants"""

import pyaudio

RATE = 48000
CHANNELS = 1
CHUNK_SIZE = 1024
WIDTH = pyaudio.paInt32

HOST = input("Enter the server IP: ")
PORT = 12024
