# to modify global variable    we have to use   'globle()'

'''
x=20
def show():
    global x
    x=30
    print(x)
    x=10
    print(x)
show()
print(x)

'''


#  use of both local and global variable...........

x=5
def disp():
    x=10
    print(x)

    p=globals()['x']
    print(p)

disp()
