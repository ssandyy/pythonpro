
a,b=int(input("enter the value of a= ")),int(input("enter the value of b= "))

p=lambda a,b:pow((a+b),2)         #  or             pow(a,2)+pow(b,2)+2*a*b
p(a,b)
print(p(a,b))