from tkinter import *
import tkinter.messagebox as m

class listbox:
    def __init__(self,w):
        self.w=w
        self.w.geometry("200x300")
        self.country=Listbox(self.w,height=3)
        self.country.insert(0,"india")
        self.country.insert(1,"srilanka")
        self.country.insert(2,"bangladesh")
        self.country.insert(3,"pakistan")
        self.country.pack()
        self.btn=Button(self.w,text="click me",command=self.selected)
        self.btn.pack()

    def selected(self):
        m.showinfo(title="country list",message="u have selected "+self.country.get(self.country.curseletion()))

w=Tk()
obj=listbox(w)
w.mainloop()