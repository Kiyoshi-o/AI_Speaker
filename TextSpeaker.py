import winsound


class ClTextSpeaker:
    def __init__(self, voiceFile):
        self.voiceFile = voiceFile

    def outputWav(self):
        with open(self.voiceFile, 'rb') as voice_f:
            data = voice_f.read()
        winsound.PlaySound(data, winsound.SND_MEMORY)
