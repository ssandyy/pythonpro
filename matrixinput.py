A=[]
B=[]
C=[]

print("enter the value of A=")
for i in range(3):
    r=[]
    for j in range(3):
        r.append(int(input()))
    A.append(r)

print("enter the value of B=")
for i in range(3):
    r=[]
    for j in range(3):
        r.append(int(input()))
    B.append(r)

for i in range(len(A)):
    r=[]
    for j in range(len(A[0])):
       r.append(A[i][j]+B[i][j])
    C.append(r)
for i in C:
    print(i)