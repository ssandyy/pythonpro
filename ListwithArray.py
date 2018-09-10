# to create an array we have to first import import package .....

import array
a=array.array('i',[1,2,3,4,5,6])
print(a[5])

b=array.array('f',[1,2,3,4,5,6])
print(b[2])
print(b)

c=array.array('d',[1,2,3,4,5,6])
print(c[1])

# we can use indexing and slicing in array also.......

del b[2]
print(b)
b.append(22)
print(b)