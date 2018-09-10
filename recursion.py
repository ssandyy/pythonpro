# W.A.P to find factorial of a no. using recursion.

n=int(input("enter the number ="))

def factorial(n):
    if n==1:
        return 1
    else:
        return (n*factorial(n-1))

print("factorial of",n,"is",factorial(n))
