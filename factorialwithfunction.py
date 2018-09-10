
'''
 In general way

a=int(input("enter the number="))

fact=1
for i in range(1,a+1):
    fact=fact*i
    print(fact)
'''

# with function==============================================================================================================


a=int(input("enter the number to find factorial ="))
def factorial():
    fact=1
    for i in range(1,a+1):
        fact=fact*i
        print(fact)

factorial()