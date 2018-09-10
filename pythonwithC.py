a,b,d=int(input("enter the value of a=")),int(input("enter the value of b=")),int(input("enter the value of d="))

c=a+b

mult=a*b*d

print("sum of", a,"and",b,"is",c)

print("sum of %d and %d is %d"%(a,b,c))  # since python is made of  C language so it support someways of C-lang...

print("sum of {} and {} is {}".format(a,b,c))

print("product of {},{} and {} is {}".format(a,b,d,mult))