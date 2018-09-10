class A:
    def show(self,x,y):
        print("class A")          
class B(A):
    def show(self):
        print("class B")
        super.show()
obj=B()
obj.show()
