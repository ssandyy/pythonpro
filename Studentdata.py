# w.a.p to store student data in a file and retrive those data from file and display..


class Student:

    def __init__(self,r,n,m):
        self.roll=r
        self.name=n
        self.marks=m

    def disp(self):
        print("Roll no. :",self.roll,"Name of student :",self.name,"Marks :",self.marks)


L=[]
r = int(input("enter the range="))
for i in range(0, r):
    s=Student(input("enter the roll="),input("enter the name="),input("enter the marks="))
    s.disp()
    L.append(s)


print()
print( "Data of ",r,"students are :\n")
for i in range(r):
    L[i].disp()