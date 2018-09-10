import pickle

class Employee:

    def __init__(self,ename,egroup,esal,eaddrs):
        self.ename=ename
        self.egroup=egroup
        self.esal=esal
        self.eaddrs=eaddrs

    def display(self):
        print("Employ name=",self.ename,"\tEmploy group=",self.egroup,"\tEmploy salary=",self.esal,"\tEmploy addrs=",self.eaddrs)
'''
s=Employee("sand","bawa",1000000,"us")
s.display()

.,...................................................OR......................................................................

'''
# with function not need to be close ..

#f=open("f:\pythonpro\Employ(withpickle).txt","wb"):

with open("f:\pythonpro\Employ(withpickle).txt","wb")as f:
    s=Employee(input("enter employ name: "),input("enter Group of employ: "),int(input("enter salary of employ:")),input("enter address: "))
    pickle.dump(s,f)
    print("picking of object is completed...")

with open("f:\pythonpro\Employ(withpickle).txt","rb")as f:
    p=pickle.load(f)
    print("unpickling of object is completed..")
    p.display()