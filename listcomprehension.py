A=[1,2,3],[4,5,6],[7,8,9]
B=[12,11,33],[44,55,66],[77,88,99]
C=[A[i][j]+B[i][j] for i in range(len(A)) for j in range(len(A[0]))]
print(C)
