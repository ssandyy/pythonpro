# W.A.P to find y=x^n by using recursion.


x,n=int(input("enter base number=")),int(input("enter power number="))
def power(x,n):
    if n==0:
        return 1
    else:
        return (x*pow(x,n-1))        # or    return pow(x,n)                     valid

y=pow(x,n)
print(y)

#      or

#print("y="power(x,n))


