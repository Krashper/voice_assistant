import speech_recognition as sr
import pyttsx3
from language import select_language

r = sr.Recognizer()
engine = pyttsx3.init()
lang = select_language()

def speak(text):
    engine.say(text)
    engine.runAndWait()


def listen():
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print('Говорите...')
        audio = r.listen(source)
        text = r.recognize_google(audio, language=lang)
        speak(text)

input('Нажмите Enter, чтобы начать')
while True:
    listen()
    input('Нажмите Enter, чтобы начать')
