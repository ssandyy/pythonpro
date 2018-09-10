x=int(input("enter the number to find square root="))

p=lambda x: x**2
'''
or
p=lambda x:pow(x,2)
'''
p(x)
print("square root of ",x,"is ",p(x))