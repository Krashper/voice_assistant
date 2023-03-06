import speech_recognition as sr
import pyttsx3
from language import select_language
import re
from datetime import datetime

r = sr.Recognizer()
engine = pyttsx3.init()
lang = select_language()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def process(text):
    if re.search(r'([Вв]рем\w+)|([Чч]ас)', text):
        now = datetime.now()

        if now.hour in (1, 21):
            hours = f'{now.hour} час'
        elif now.hour in (2, 3, 4, 22, 23):
            hours = f'{now.hour} часа'
        else:
            hours = f'{now.hour} часов'
        
        if now.minute in range(10, 20) or (now.minute % 10) in (0, 5, 6, 7, 8, 9):
            minutes = f'{now.minute} минут'
        elif now.minute % 10 == 1:
            minutes = f'{now.minute} минута'
        else:
            minutes = f'{now.minute} минуты'
        speak(f'Сейчас {hours} {minutes}')


def listen():
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print('Говорите...')
        audio = r.listen(source)
        text = r.recognize_google(audio, language=lang)
        process(text)

input('Нажмите Enter, чтобы начать')
while True:
    listen()
    input('Нажмите Enter, чтобы начать')
