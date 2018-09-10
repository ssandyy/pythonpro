# Q> w.a.p to multiply two matrix   1. by normal loop      2. by list comprehension...

A=[]
B=[]
C=[]


print("enter the value of matrix A =")
for i in range(3):
    for j in range(3):
        A.append(int(input()))

print("enter the value of matrix B=")
for i in range(3):
    for j in range(3):
        B.append(int(input()))

print("A=",A)
print("B=",B)

C=[A[i][j]+B[i][j] for i in range(len(A)) for j in range(len(A[0]))]

print("Addition of A and B= ",C)
