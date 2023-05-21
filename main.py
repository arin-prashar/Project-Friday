from bardapi import Bard
import os
import audio
from dotenv import load_dotenv
from audio import prompt,speak
import mail as m

load_dotenv()
os.environ["_Bard_API_KEY"]=os.getenv("api")
client = Bard()
def Friday():
    while True:
        question = audio.prompt()
        if question == "bye" or question == "goodbye" or question == "exit" or question == "Bye" or question == "Goodbye" or question == "Exit" or question == "bye." or question == "goodbye." or question == "exit.":
            audio.speak("Bye, Have a nice day.")
            return 'exit'
            break
        if question=="Google Speech Recognition could not understand audio":
            audio.speak("Can you please ask it again.")
            continue
        else:
            if question.startswith("do"):
                tsk = question[3:]
                task(tsk)
            elif question.startswith("tell"):
                res = client.get_answer(question)['content']
                audio.speak(res)
            
def task(tsk):
    audio.speak("What task is to be done?")
    tsk=audio.prompt()
    tsk.lower()
    if tsk.startswith("send mail"):
        audio.speak("Whom to send mail?")
        to = audio.prompt()
        audio.speak("What is the subject?")
        subject = audio.prompt()
        audio.speak("What is the message?")
        msg=audio.prompt()
        m.gmail_create_draft(to,subject,msg)
        audio.speak("Draft created")
    # if task contains play music play music
    elif tsk.startswith("play music"):
        # open spotify to play music
        audio.speak("Opening spotify")
        os.system("spotify")
    # if task contains open browser open browser
    elif tsk.startswith("open browser"):
        # open browser
        audio.speak("Opening browser")
        os.system("Chrome")
    elif tsk.startswith("save to file"):
        audio.speak("What to save?")
        text = audio.prompt()
        audio.speak("What is the file name?")
        file_name = audio.prompt()
        audio.write(text,file_name)

while True:
    if audio.prompt() == "Friday":
        audio.speak("Yes sir, How can I help you?")
        Friday()
        break