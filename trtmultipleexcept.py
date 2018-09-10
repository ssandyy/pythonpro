try:
    print("enter 1st no. ")
    a=int(input())
    print("enter 2nd no. ")
    b=int(input())
    c=a/b
    print(c)
except ZeroDivisionError:
	print("plz don't divide by Zero..")
except ValueError:
	print("enter the value in interger..")
