#from pip._vendor.distlib.compat import raw_input

a=input("enter to check pallindrom or not =")
if(a==a[::-1]):
    print("given input is pallindrom")
else:
    print("given input  is not pallindrom")