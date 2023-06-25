from bardapi import Bard
import os
import audio
from dotenv import load_dotenv
from audio import prompt,speak


def Friday():
    load_dotenv()
    os.environ["_Bard_API_KEY"]=os.getenv("api")
    client = Bard()
    while True:
        question = audio.prompt("1")
        if question == "bye" or question == "goodbye" or question == "exit" or question == "Bye" or question == "Goodbye" or question == "Exit" or question == "bye." or question == "goodbye." or question == "exit.":
            audio.speak("Bye, Have a nice day.")
            return 'exit'
            break
        if question=="Google Speech Recognition could not understand audio":
            audio.speak("Can you please ask it again.")
            continue
        res=client.get_answer(question)['content']
        print(res)
        
