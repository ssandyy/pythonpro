
# we can assign new name to available function ......

def show():
    print('hello')


disp=show

disp()

print(id(show),id(disp))