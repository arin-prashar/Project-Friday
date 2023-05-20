import tkinter as tk
import ttkbootstrap as ttk
import main as Brain
import audio
from audio import prompt,speak

def ask():
    while True:
        if audio.prompt()=="Friday":
            audio.speak("Hello, I am Friday. How can I help you?")
            while True:
                res=Brain.Friday()
                if res=="exit":
                    exit()
                else:
                    output_string.set(res)
                    output_label.pack(pady=5)   



window=ttk.Window(themename='cyborg')  
window.title("Friday Test")
window.geometry("400x100")
title_label = ttk.Label(master=window, text="Project Friday",font='Arial 24 bold')
title_label.pack()
output_string=tk.StringVar()
output_label = ttk.Label(master=window,text="Miles: ",font='Garet 20',textvariable=output_string,command=ask())
output_label.pack(pady=5)
window.mainloop()
