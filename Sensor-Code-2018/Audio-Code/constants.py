# TCP Constants
import pyaudio

RATE = 48000
CHANNELS = 1 # The pi microphone unfortunately has only one channel.
CHUNK_SIZE = 1024
WIDTH = pyaudio.paInt32 # If the interpreter cannot recognice what this constant is, then you have the wrong version of pyaudio.

HOST = input("Enter the server IP: ")
PORT = 12024
