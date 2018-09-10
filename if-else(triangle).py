l=int(input("enter the length of triangle="))
b=int(input("enter the bredth of triangle="))
h=int(input("enter the hypotenous of triangle="))

if (l==b &b==h):
    print("this is equilateral triangle")
elif(l !=b & b!=h & h!=l):
    print("this is scalan triangle")
else:
    print("this is isolated triangle")     # if two sides are equal