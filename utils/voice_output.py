import pyttsx3

class VoiceOutput:
    def __init__(self, rate=180, volume=1.0, voice=None):
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', rate)
        self.engine.setProperty('volume', volume)
        if voice:
            self.engine.setProperty('voice', voice)

    def speak(self, text):
        if isinstance(text, list):
            for line in text:
                self.engine.say(line)
        else:
            self.engine.say(text)
        self.engine.runAndWait()
