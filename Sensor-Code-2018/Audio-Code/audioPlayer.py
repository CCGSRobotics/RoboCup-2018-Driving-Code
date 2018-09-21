class AudioPlayer:
    # Plays a single chunk of audio data
    def __init__(self, chunksize, width, rate, channels):
        self.audioClient = pyaudio.PyAudio()
        self.audioData = ""
        self.chunksize = chunksize
        self.width = width
        self.rate = rate
        self.channels = channels

        self.stream = self.audioClient.open(
            format=self.width,
            channels=self.channels,
            rate=self.rate,
            output=True
        )

    # Play the entire byte string
    def play(self):
        self.stream.write(self.audioData)

    # Close the audio streams
    def close(self):
        self.stream.close()
        self.audioClient.terminate()
