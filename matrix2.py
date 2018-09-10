#  Q  w.a.p to add two matrix .

A=[1,2,3],[4,5,6],[7,8,9]
B=[11,22,33],[44,55,66],[77,88,99]
C=[0,0,0],[0,0,0],[0,0,0]

for i in range(3):
    for j in range(3):
        C[i][j] = A[i][j] + B[i][j]
        print(C[i][j],end=' ')
    print()

print()

#.........................OR.............................................................

D=[]

for i in range(len(A)):
    r=[]
    for j in range(len(A[0])):
       r.append(A[i][j]+B[i][j])
    D.append(r)
for i in D:
    print(i)