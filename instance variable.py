# use of instance variable
# instance variable can be defined under constructor(__init__)    with "self" keyword
#.............................................................................................................



class Student:
    def __init__(self,name,roll,marks):
        self.name=name;         # decleration of instance variable
        self.roll=roll;
        self.marks=marks;

    def display(self):
        print("Student name :",self.name)    #  call of instance variable
        print("Student roll :",self.roll)
        print("Student marks :",self.marks)

        #          OR.............................
        print()
        print("Student name :",self.name,"Student roll :",self.roll,"Student marks :",self.marks)


s1=Student("hellboy",123,99)
s1.display()


#   __dict__   use to call automatically the variable by going through argument demands...

print()
print(s1.__dict__)