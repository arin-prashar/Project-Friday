import speech_recognition as sr
import pyttsx3
import pyautogui
import os
import time
def prompt():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
    try:
        print(r.recognize_google(audio))
        return r.recognize_google(audio)
    except sr.UnknownValueError:
        # print("Google Speech Recognition could not understand audio")
        return "Google Speech Recognition could not understand audio"
    except sr.RequestError as e:
        # print("Could not request results from Google Speech Recognition service; {0}".format(e))
        return "Could not request results from Google Speech Recognition service; {0}".format(e)

def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(text)
    engine.runAndWait()
    # return
def write(text,file_name):
    # os.system("notepad")
    time.sleep(2)
    with open(file_name+".txt","w") as f:
        f.write(text)
    f.close()
    return

# write(prompt(),prompt())