
from heapq import merge

n1 = 0
n2 = 1
c = 0

n= int(input("Enter upper range: "))
for i in range(c,n + 1):

   if i > 1:
       for j in range(2,i):
           if (i % j) == 0:
               break
       else:
           print(i,end=',')

while c < n:
    if (n1 % 2 != 0):
        print(n1,end=' , ')
    nth= n1 + n2
    n1 = n2
    n2 = nth
    c =c+1
'''
z=list(num , n1)
print(z)
'''