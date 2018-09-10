class Student:
    def input(self,n,r,m):
        self.name=n
        self.roll=r
        self.mark=m
    def disp(self):
        print(self.name,self.roll,self.mark)

s1=Student()
s1.input(input("enter sudent1 name= "),int(input("enter student roll= ")),int(input("enter student marks= ")))
s1.disp()
s2=Student()
s2.input(input("enter sudent2 name= "),int(input("enter student roll= ")),int(input("enter student roll= ")))
s2.disp()
