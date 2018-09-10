import logging

logging.basicConfig(filename="exceptionhandling(withlogging).log",level=logging.DEBUG)

logging.info("execution starts")
try:
    x=int(input("enter first number :"))
    y=int(input("enter second number :"))
    print(x/y)

except ZeroDivisionError as msg:
    print("Number cannot be divisible by zero.....")

    logging.exception(msg)
except ValueError as msg:
    print("please enter only integer value..")

    logging.exception(msg)
finally:
    logging.info("execution over....")