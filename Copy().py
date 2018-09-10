#   we can copy elements in two ways    "deep copy"   and   "shallow copy"............

#deep copy :-

A=[1,2,3,4,5]
B=A
print("A= ",A,"B= ",B)
#print(B)

B.append(9)
print("A= ",A,"B= ",B)        #  A=  [1, 2, 3, 4, 5, 9] B=  [1, 2, 3, 4, 5, 9]



# shallow copy .............................
print()

X=[11,22,33,44,55]
Y=X[:]
#Y=X.copy()
print("X= ",X,"Y= ",Y)

Y.append(99)
print("X= ",X,"Y= ",Y)     #  X=  [11, 22, 33, 44, 55] Y=  [11, 22, 33, 44, 55, 99]