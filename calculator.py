from tkinter import *
w=Tk()
w.geometry("200x200")




v=StringVar()
expression=""

def btnclk(n):
    global expression
    expression +=str(n)
    v.set(expression)
def equals():
    global expression
    result=eval(expression)
    v.set(result)
def clear():
    global expression
    expression=""
    v.set(expression)


#row1( screen)

entry=Entry(w,bg="yellow" ,bd=4 ,textvariable=v,justify="right")
entry.grid(row=1,column=1,columnspan=4)

btn1=Button(w,text='1',command=lambda:btnclk(1))
btn2=Button(w,text='2',command=lambda:btnclk(2))
btn3=Button(w,text='3',command=lambda:btnclk(3))
btn4=Button(w,text='4',command=lambda:btnclk(4))
btn1.grid(row=2,column=1)
btn2.grid(row=2,column=2)
btn3.grid(row=2,column=3)
btn4.grid(row=2,column=4)

btn5=Button(w,text='5',command=lambda:btnclk(5))
btn6=Button(w,text='6',command=lambda:btnclk(6))
btn7=Button(w,text='7',command=lambda:btnclk(7))
btn8=Button(w,text='8',command=lambda:btnclk(8))
btn5.grid(row=3,column=1)
btn6.grid(row=3,column=2)
btn7.grid(row=3,column=3)
btn8.grid(row=3,column=4)

btn9=Button(w,text='9',command=lambda:btnclk(9))
btn0=Button(w,text='0',command=lambda:btnclk(0))
btneq=Button(w,text='=',command=lambda:equals())
btnclr=Button(w,text='C',command=lambda:clear())
btn9.grid(row=4,column=1)
btn0.grid(row=4,column=2)
btneq.grid(row=4,column=3)
btnclr.grid(row=4,column=4)

btnplus=Button(w,text='+',command=lambda:btnclk("+"))
btnmin=Button(w,text='-',command=lambda:btnclk("-"))
btndiv=Button(w,text='/',command=lambda:btnclk("/"))
btnmul=Button(w,text='*',command=lambda:btnclk("*"))
btnplus.grid(row=5,column=1)
btnmin.grid(row=5,column=2)
btndiv.grid(row=5,column=3)
btnmul.grid(row=5,column=4)

w.mainloop()