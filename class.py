n="hello"
r=12
class Test:
    def print(self,n,r):
        self.n=n
        self.r=r
    def disp(self):
        print(self.n,self.r)

s=Test()
s.print(input("enter yoyr name :"),int(input("enter your roll ")))
s.disp()
