# format() is method of string class use to assign the value to the string.


a,b=int(input("enter the value of a=")),int(input("enter the value of b="))

c=a+b
d=a/b
m=a*b

print("sum of {} and {} is {}".format(a,b,c))

print("sum of {0} and {1} is {2}".format(a,b,c))

print("sum of {1} and {2} is {0}".format(a,b,c))

print()

print("division of {} and {} is {}".format(a,b,d))

print("multiplication of {} and {} is {}".format(a,b,m))

