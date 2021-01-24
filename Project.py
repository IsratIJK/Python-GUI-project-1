from tkinter import *
window=Tk()
window.geometry('500x500+150+300')
window.title('Hello! This is my first project')
b=Button(text='Hello! This is my first project',relief=SUNKEN).grid()
b=Button(text='Hello! This is my first project',relief=FLAT).grid()
b=Button(text='Hello! This is my first project',relief=GROOVE).grid()
b=Button(text='Hello! This is my first project',relief=RAISED).grid()
b=Button(text='Hello! This is my first project',relief=RIDGE).grid()
l=Label(text='Hello! This is my first project',fg='red',bg='blue').grid(row=1,column=1)
# we can't use grid() and pack() at a time.
window.mainloop()
