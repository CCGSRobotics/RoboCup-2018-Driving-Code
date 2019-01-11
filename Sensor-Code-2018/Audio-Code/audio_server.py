"""A pyaudio callback server"""

import socket
from audio_player import AudioPlayer
import constants

def main():
    """audio_server.py: main function"""
    player = AudioPlayer(constants.CHUNK_SIZE, constants.WIDTH, constants.RATE, constants.CHANNELS)

    socket_client = socket.socket()
    socket_client.bind(("", constants.PORT))

    socket_client.listen(1)
    client, address = socket_client.accept()

    print("Audio Connection from:", str(address))

    while True:
        data = client.recv(8192)
        if not data:
            break

        player.audio_data = data
        player.play()

    client.close()
    player.close()

main()
