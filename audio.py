import speech_recognition as sr
import pyttsx3
import pyautogui
import os
import time
def prompt(type):
    ask="."
    if type == "0":
        ask = "."
    elif type == "1":
        ask='What is your question?'
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print(ask)
        audio = r.listen(source)
    try:
        if audio=="exit" or audio=='Exit' or audio=="EXIT":
            return
        print(r.recognize_google(audio))
        return r.recognize_google(audio)
    except sr.UnknownValueError:
        return "Google Speech Recognition could not understand audio"
    except sr.RequestError as e:
        return "Could not request results from Google Speech Recognition service; {0}".format(e)

def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(text)
    engine.runAndWait()