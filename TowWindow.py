from tkinter import *
old = Tk()
new = Tk()
def hello():
    m = b.get()
    L=Label(text='enter', fg='yellow',bg='orange',font=10).pack()
def delete():
    L2=Label(text='delete', fg='orange',bg='yellow',font=10).pack()
old.geometry('500x500+100+200')
new.geometry('500x500+700+200')
old.title('Hello World')
new.title('Hello Tkinter')
b=StringVar()
MyLabel=Label(text='Welcome',fg='#646060',bg='#F87217',font=10).pack()
MyButton1=Button(text='Enter',fg='gray',bg='plum',command=hello,font=20).pack()
MyButton2=Button(text='Delete',fg='gray',bg='plum',font=20).pack()

text=Entry(textvariable=b).pack()
old.mainloop()
