from PIL import Image,ImageTk
import datetime
from tkinter import *
import tkinter as tk
import self


w=tk.Tk()

w.geometry('300x500')
w.title("age_calculator")

year_label=tk.Label(text="year")
year_label.grid(column=0,row=1)

month_label=tk.Label(text="month")
month_label.grid(column=0,row=2)

day_label=tk.Label(text="day")
day_label.grid(column=0,row=3)

year_Entry=tk.Entry()
year_Entry.grid(column=1,row=1)

month_Entry=tk.Entry()
month_Entry.grid(column=1,row=2)

day_Entry=tk.Entry()
day_Entry.grid(column=1,row=3)

def calculator_age():
   print(year_Entry.get())
   print(month_Entry.get())
   print(day_Entry.get())
   person=Person('Qazi',datetime.date(int(year_Entry.get()),int(month_Entry.get()),int(day_Entry.get())))
   print(person.age())
   text_answer=tk.Text(master=window, height=20,width=30)

calculate_button=tk.Button(text="Calculate Now!",command=calculator_age )
calculate_button.grid(column=1,row=5)

class Person:
   def __init__(self,name,birthdate):
      self.name=name
      self.birthdate=birthdate

   def age(self):
      today=datetime.date.today()
      age=today.year - self.birthdate.year
      return age


w.mainloop()