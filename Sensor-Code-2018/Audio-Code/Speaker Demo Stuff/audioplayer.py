class AudioPlayer:
    """ Plays a single chunk of audio data """ 
    def __init__(self, chunksize, width, rate, channels):
        """ Init audio stream """ 
        self.p = pyaudio.PyAudio()

        self.audioData = "" # This is mutable
        self.chunksize = chunksize
        self.width = width
        self.rate = rate
        self.channels = channels

        self.stream = self.p.open(
            format = self.width,
            channels = self.channels,
            rate = self.rate,
            output = True
        )

    def play(self):
        """ Play entire BYTE STRING """
        self.stream.write(self.audioData)

    def close(self):
        """ Graceful shutdown """ 
        self.stream.close()
        self.p.terminate()
