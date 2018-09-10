from tkinter import *
import tkinter.messagebox as m

w=Tk()

def buttton():
    m.showwarning(title="message",message="hello")
    m.showerror(message="error-message")
    m.showinfo(message="information ")

btn=Button(w,text="submit",command=buttton)
btn.grid(row=0,column=1)

w.mainloop()