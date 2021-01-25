from tkinter import *
window=Tk()
window.geometry('500x500+150+300')
window.title('Hello! This is my first project')
b=Button(text='Hello! This is my first project',width=30,height=24,bg="blue",fg="white",activebackground="red",activeforeground="pink",bd=30,cursor="heart").grid()
l=Label(text='Hello! This is my first project',fg='red',bg='blue').grid(row=1,column=1)
# we can't use grid() and pack() at a time.
window.mainloop()
