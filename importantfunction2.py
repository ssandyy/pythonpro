# count(),index(),remove(),pop(),pop(index),reverse(),sort()


# count() :-   use to count the number of elements present

A=[1,2,3,4,4,1,21,2,4,1,3,45,5,1,2,2,3,22,1,1,2,3,4,]
print(A.count(1))


#index() :-  use to know the position of the elements (it always give first occurence of element)
print()
B=[10,20,30,40,50,10]
print(B.index(10))



# pop() :- it will remove the element from last position
print()

C=[1,2,3,4,5]
print("Before using pop()  C= ",C)
print(C.pop())
print("after using pop()   C= ",C)


#pop(index) :- it will remove the element from specific position.....by index position
print()


D=[11,22,33,44,55]
print("before using pop(index)   D= ",D)
print(D.pop(2))
print("after using pop(index)   D= ",D)


# remove() :- use to remove the element as required  (it remove the elements with first occurence) ....

print()

E=[10,20,30,40,50,60,10,2,1,20,10,40,30]
print(E)
E.remove(10)
print(E)


# reverse() :- use to reverse the entire elements
print()


F=[1,2,3,3,4,4,6,6,77,8,9]
print("f before use of reverse() =",F)
F.reverse()
print("f after use of reverse() =",F)


#sort():- use to sort(bring in assending order) of elements
print()
print()

print("f before use of sort() =",F)
F.sort()
print("f after use of sort() =",F)