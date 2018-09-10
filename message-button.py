from tkinter import *
import tkinter.messagebox as m

w=Tk()
w.title("dynamic button")
w.geometry("400x450")

def go():
    m.showinfo(message="hello")

btn=Button(w,text="click",command=go)
btn.pack()

w.mainloop()