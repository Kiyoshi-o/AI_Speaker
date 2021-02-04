import speech_recognition as Srecog


class ClVoiceRecognition:
    @staticmethod
    def voiceToText():
        result = ""
        print("Say Something ...")

        with Srecog.Microphone() as source:
            Srecog.Recognizer().adjust_for_ambient_noise(source)
            audio = Srecog.Recognizer().listen(source)

            print("Now to recognize it ...")

        try:
            result = Srecog.Recognizer().recognize_google(audio, language='ja-Jp')
            print(result)
            return True, result

            # 以下は認識できなかったときに止まらないように。
        except Srecog.UnknownValueError:
            print("could not understand audio")
            return False, result

        except Srecog.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
            return False, result
