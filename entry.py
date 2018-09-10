from tkinter import *
from tkinter import messagebox as m

w=Tk()
w.title("entry-grid")
w.geometry("500x600")

def sub():
    m.showinfo(message="hello")


name=Label(w,text="Name")
password=Label(w,text="password")
name.grid(row=0,column=1,sticky=E)
e1=Entry(w)
e1.grid(row=0,column=2)
password.grid(row=1,column=1)
e2=Entry(w)
e2.grid(row=1,column=2)


button=Button(w,text="click me",command=sub)
button.grid(row=3,column=2)


w.mainloop()