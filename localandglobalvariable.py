
x=10 # global variable ......................

def add():
    x=20 # local variable ...................
    print(x)

print(x)
add()
def show():
    print(x)

show()