import os
import requests


class ClSpeechSynthesis():
    VoiceTextWeb_API = "zjbjkyglhm1r2kv8"

    def __init__(self, fileName, text, speaker, emotion, emotion_level, pitch, speed, volume):
        self.file = fileName + ".wav"
        self.text = text
        self.speaker = speaker
        self.emotion = emotion
        self.emotion_level = emotion_level
        self.pitch = pitch
        self.speed = speed
        self.volume = volume

    def getVoice(self):
        adress = 'https://api.voicetext.jp/v1/tts'
        Parameters = {
            'text': self.text,
            'speaker': self.speaker,
            'emotion': self.emotion,
            'emotion_level': self.emotion_level,
            'pitch': self.pitch,
            'speed': self.speed,
            'volume': self.volume
        }
        filePath = os.path.abspath(self.file)
        send = requests.post(adress, params=Parameters, auth=(self.VoiceTextWeb_API, ''))
        result = open(filePath, 'wb')
        result.write(send.content)
        result.close()

        return filePath
