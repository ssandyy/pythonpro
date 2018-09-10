A=[10,20,30,40,50]
try:
    n=int(input("enter the position ...."))
    if n>A:
        
        for i in A:
            print(i)
except IndexError:
    print("plx enter valid position ")
