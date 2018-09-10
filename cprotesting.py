A=[]
B=[]
C=[]

for i in range(3):
    r=[]
    for j in range(3):
        r.append(input("enter the element of first matrix="))
    A.append(r)

for i in range(3):
    r=[]
    for j in range(3):
        r.append(input("enter the element of second matrix="))
    B.append(r)

for i in range(len(A)):
    r=[]
    for j in range(len(A[0])):
        r.append(A[i][j]+B[i][j])
    C.append(r)

for k in range(3):
    print(C[k])