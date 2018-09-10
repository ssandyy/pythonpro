from tkinter import *

w=Tk()
w.title("frame")
w.geometry("300x400")

topframe=Frame(w)
bottomframe=Frame(w)
topframe.pack()
bottomframe.pack(side=BOTTOM)

button1=Button(topframe,text="click me",bd=8)
button1.pack()
button2=Button(bottomframe,text="submit",fg="blue")
button2.pack()
button3=Button(w,text="reset",bg="green")
button3.pack(side=LEFT)
button4=Button(w,text="save",bg="purple")
button4.pack(side=RIGHT)


w.mainloop()