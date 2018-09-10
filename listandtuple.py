#  list are mutable but tuple are imutable....

# list take more space then tuple for same work...

import sys
a_list=[1,2,3,4,5,6,7,8,9]
print("size used by list=",sys.getsizeof(a_list))

b_tuple=(1,2,3,4,5,6,7,8,9)
print("size used by tuple=",sys.getsizeof(b_tuple))


print()
# tuple takes less time then list to execute....

import timeit
t_list=timeit.timeit(stmt="[1,2,3,4,5,6,7,8,9]",number=100000)
print("time used by list=",t_list)

t_tuple=timeit.timeit(stmt="(1,2,3,4,5,6,7,8,9)",number=100000)
print("time used by tuple=",t_tuple)