f=open("F:\pythonpro/filehandlingtest.py",'r')
print(f.read())
f=open("F:\pythonpro/filehandlingtest.py",'w')
f.write("python world")
f=open("F:\pythonpro/filehandlingtest.py",'r')
print(f.read())
f.close()