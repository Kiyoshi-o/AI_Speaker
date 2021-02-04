import sys
import VoiceRecognition
import SpeechSynthesis
import GetReply
import TextSpeaker
import random as rd  # TestCode

from VoiceRecognition import ClVoiceRecognition


def main():
    speaker = "takeru"
    emotionList = ["happiness", "anger", "sadness"]
    pitch = 100
    speed = 100
    volume = 100

    print("*** AI自動返信開始 ***")
    # print("([E]を押して終了)")

    while True:
        root_vR: ClVoiceRecognition = VoiceRecognition.ClVoiceRecognition()  # インスタンス生成
        result = root_vR.voiceToText()
        if bool(result[0]):
            root_gR = GetReply.ClGetReply(result[1])  # インスタンス生成
            reply = root_gR.getReply()
        else:
            reply = "すみません。よく分かりません。"

        # TestCode 感情(ランダム)
        emotion = emotionList[rd.randint(0, 2)]
        emotion_level = rd.randint(1, 4)
        # TestCode_END

        root_sS = SpeechSynthesis.ClSpeechSynthesis(
            "voice", reply, speaker, emotion, emotion_level, pitch, speed, volume)  # インスタンス生成
        voiceFile = root_sS.getVoice()
        root_tS = TextSpeaker.ClTextSpeaker(voiceFile)  # インスタンス生成
        root_tS.outputWav()

        if not bool(result[0]):
            sys.exit()


if __name__ == '__main__':
    main()
