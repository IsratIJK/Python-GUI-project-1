from tkinter import *
MyGui = Tk()
def hello():
    m=b.get()
    L=Label(text='b', fg='yellow',bg='orange',font=10).pack()
def delete():
    L2=Label(text='delete', fg='orange',bg='yellow',font=10).pack()
MyGui.geometry('500x500+300+200')
MyGui.title('Hello World')
b=StringVar()
MyLabel=Label(text='Welcome',fg='#646060',bg='#F87217',font=10).pack()
MyButton1=Button(text='Enter',fg='gray',bg='plum',command=hello,font=20).pack()
MyButton2=Button(text='Delete',fg='gray',bg='plum',font=20).pack()
text=Entry(textvariable = b).pack()

MyGui.mainloop()
