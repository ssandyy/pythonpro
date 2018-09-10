from tkinter import *

w=Tk()
w.title('image')
w.geometry('400x200')

menubar=Menu(w)
w.configure(menu=menubar)

filemenu=Menu(menubar)
filemenu.add_command(label='New')
filemenu.add_command(label='open')
filemenu.add_command(label='close')


menubar.add_cascade(label='File',menu=filemenu)

img=PhotoImage(file='F:\imgg.gif',height=100,width=50)
lb1img=Label(w,image=img)
lb1img.grid(row=1,column=1,rowspan=2)

w.mainloop()
