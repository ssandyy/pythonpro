class NegativeNumberError(Exception):
    pass

    try:
        print("enter the number...")
        n=int(input())
        if n<0:
            raise NegativeNumberError
        print(n)
    except NegativeNumberError:
        print("please enter positive number....")
