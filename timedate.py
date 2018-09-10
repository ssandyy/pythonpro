import csv
import datetime

#print(dir(datetime))

print()
aaj=datetime.datetime.today()
print(aaj)
print(aaj.day)
print(aaj.month)
print(aaj.min)
print(aaj.microsecond)
tarik=datetime.date.today()
print(tarik)
ttime=datetime.time()

print(ttime)

print(aaj.strftime("%A,%d %B,%Y"))   # %A for full day name, %d for number of date, %B full name of month,%Y for year
message="todays date is {:%A,%d %B,%Y}."
print(message.format(aaj))