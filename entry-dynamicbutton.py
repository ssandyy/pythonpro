from tkinter import *
import tkinter.messagebox as m

w=Tk()
w.title("entry with button")
w.geometry("200x200")
t1=Label(w,text="Name:")
t1.grid(row=0,column=1,sticky=E)
e1=Entry(w)
e1.grid(row=0,column=2)
t2=Label(w,text="Password:")
t2.grid(row=1,column=1)
e2=Entry(w)
e2.grid(row=1,column=2)

def submit():
    v=m.askyesno(title="submit",message="Do u want to proceed..?")

    if v==True:
        m.showinfo(message="welcome to python galaxy")
    else:
        m.showwarning(message="you will be exited..")

btn=Button(w,text="submit",command=submit)
btn.grid(row=2,column=2)

w.mainloop()