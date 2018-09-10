#"w" is for write

f=open("f:/pythonpro/write.txt",'w')
f.write("hello file handling..in python")
print(f.name)  # it is use to show the path
print(f.mode)  # it is use to show the mode weather file is in read(r) mode or write(w)
f.close()

print()
print()
# "r " is for read
f=open("f:/pythonpro/write.txt",'r')
print(f.read())
print(f.name)     # it is use to show the path
print(f.mode)      # it is use to show the mode weather file is in read(r) mode or write(w)
f.close()

f=open("f:/pythonpro/write.txt",'w')
f.write("welcome to python world.....")
f.close()

f=open("f:/pythonpro/write.txt",'r')
print(f.read())
f.close()


#" a" mean append
f=open("f:/pythonpro/write.txt",'a')
f.write(" programing")
f.close()
f=open("f:/pythonpro/write.txt",'r')
print(f.read())
f.close()