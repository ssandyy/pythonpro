try:
    n=int(input("enter first number.."))
    if n>5:
        raise ValueError
    print(n)
except ValueError:
    print("please enter value smaller  then 5")
    
