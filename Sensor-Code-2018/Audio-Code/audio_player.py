import pyaudio

class AudioPlayer(pyaudio.PyAudio):
    """An audio player transferring audio data from audio_client.py to audio_server.py"""

    def __init__(self, chunksize, width, rate, channels):
        """Initialise all variables and the pyaudio.PyAudio super"""
        super().__init__()
        self.audio_data = ""
        self.chunksize = chunksize
        self.width = width
        self.rate = rate
        self.channels = channels

        self.stream = super().open(
            format=self.width,
            channels=self.channels,
            rate=self.rate,
            output=True
        )

    def play(self):
        """Play the entire byte string"""
        self.stream.write(self.audio_data)

    def close(self):
        """Close the audio stream"""
        self.stream.close()
        super().terminate()
