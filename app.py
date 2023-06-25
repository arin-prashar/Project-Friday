import tkinter as tk
import ttkbootstrap as ttk
from tkinter import *
from PIL import Image, ImageTk
import audio
from audio import prompt,speak


window=ttk.Window(themename='cyborg')  
window.title("Friday Test")
window.geometry("500x250")
window.iconbitmap('assests/F.R.I.D.A.Y.ico')

# add the title
title = ttk.Label(window, text="Welcome to Friday Test", font=("Arial Bold", 20))
title.grid(column=0, row=0)

# add the image
image = Image.open("assests/F.R.I.D.A.Y.jpg")
image = image.resize((100, 100), Image.LANCZOS)
photo = ImageTk.PhotoImage(image)
label_image = ttk.Label(window, image=photo)
label_image.grid(column=1, row=0)

# add the circular mic button
mic = ttk.Button(window, text="Mic", style="success.Outline.TButton")
mic.grid(columnspan=2, row=1)

window.mainloop()