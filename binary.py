f=open("f:/pythonpro/binnary.txt",'w')      # create .txt file
f.write("hello python")
f.close()

f=open("f:/pythonpro/binnary.txt",'wb')
f.write("hello python".encode())
f.close()

f=open("f:/pythonpro/binnary.txt",'r')
print(f.read())
f.close()