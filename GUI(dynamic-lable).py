from tkinter import *

w=Tk()
w.title("dynamic-label")
w.geometry("400x600")

one=Label(w,text="hello",bg="yellow",height=10,width=15)
one.pack()
two=Label(w,text="world",bg="purple")
two.pack(fill=X)
button=Button(w,text="click here",bg="pink")
button.pack(side=RIGHT,fill=Y)
three=Label(w,text="welcome to python galaxy",bg="green")
three.pack(side=LEFT,fill=Y)

w.mainloop()
