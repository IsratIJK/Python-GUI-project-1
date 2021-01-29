from tkinter import *
master=Tk()
master.geometry('500x500')
S1=Scale(master,from_=0,to=100)
S1.set(45)
S1.pack()
S2=Scale(master, from_=30,to=300,resolution=0.5)
S2.pack()
master.mainloop()