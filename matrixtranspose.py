A=[1,2,3],[4,5,6],[7,8,9]
for i in range(3):
    print(A[i])
B=[A[i][j] for j in range(len(A)) for i in range(len(A[0]))]

print(B)
