#    use of       append(),extend(),clear()

L=[1,2,3,4,5,6]
print(L)

L.append(77)
print(L)

L.extend([11,22,33,44,55])
print(L)

L.extend({0.1,0.2,0.3,0.4,0.5})     # set has no sequence to give output......
print(L)

L.clear()
print(L)