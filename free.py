from datetime import *
today=datetime.today()

print("Today is : ",today)



for attr in ['day','month','year','hour','minute','second','microsecond']:
    print(attr,':\t',getattr(today,attr))
   #print('Time:',today.hour,today.minute,today.second,sep=':')



day=today.strftime('%A')
month=today.strftime('%B')
year=today.strftime('%Y')
time=today.strftime('%X')
p = today.strftime('%p')
print('Date:',day,today.day,month,year,time)
print('time:', time, p)