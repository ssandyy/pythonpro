# display the data of 10 students

class Student:
    def input(self,n,r,m):
        self.name=n
        self.roll=r
        self.marks=m

    def disp(self):
        print(self.name,self.roll,self.marks)

L=[]
for i in range(10):
    s=Student()
    s.input(input("enter student name= "),int(input("enter student roll= ")),int(input("enter student marks= ")))
    s.disp()
    L.append(s)

for i in range(10):
    L[i].disp()
