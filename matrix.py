A=[[1,2,3],[4,5,6],[7,8,9]]
for i in range(len(A)):
	print(A[i])
print()

# ...............................OR.............................

for i in A:
	print(i)

print()
#...............................OR...............................

for i in range(len(A)):
	for j in range(len(A)):
		print(A[i][j],end=' ')
	print()