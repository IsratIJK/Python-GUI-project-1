from tkinter import *
from tkinter import ttk
window=Tk()
button=ttk.Button(window,text="Click Me")
button.pack()
def callback():
    print('Photo')
button.config(command=callback)
logo=PhotoImage(file='Tkinter.gif')
button.config(image=logo)