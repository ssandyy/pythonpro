'''
Q. write a print to add two no. by giving input from keyboard .

a,b=int(input("enter first value = ")),int(input("enter second value = "))
print("addition of first and second value = ",a+b)

'''


'''
Q . write a program to find the greater no. among two nos.
a,b=int(input("enter first number = ")),int(input("input second number = "))

if a>b:
    print(a,"is greater then",b)
else:
    print(b,"is greater then ",a)

'''

#-----------------------------------------------------------------------------------------------------------------------

'''
Q > W.A.P to find  number is even or odd by giving input from keyboard .

a=int(input("enter the number = "))

if a%2:
    print("value is odd..")
else:
    print("value is even...")
'''
#-----------------------------------------------------------------------------------------------------------------------

'''Q > W.A.P to find greater among 4nos using if ,elif . by giving input from keyboard.

a,b,c,d=int(input("enter the value of a= ")),int(input("enter the value of b= ")),int(input("enter the value of c= ")),int(input("enter the value of d= "))

if a>b and a>c and a>d:
    print("a is graeter ")

elif b>a and b>c and b>d:
    print("b is greater")

elif c>a and c>b and c>d:
    print("c is greater")

else:
    print("d is greater....")

'''

#-----------------------------------------------------------------------------------------------------------------------------

'''
Q > W.A.P to check no. is +ve ,-ve , or 0  giving input from keyboard.

a=int(input("enter the number = "))

if a>0:
    print("number is positive...")
elif a<0:
    print("number is negetive...")
else:
    print("enter number is zero...")

'''

#---------------------------------------------------------------------------------------------------------------------------

'''
Q > W.A.P to find greater among 3no. by giving input keyboard (using if-else).

a,b,c=int(input("enter the value of a =")),int(input("enter the value of b=")),int(input("enter the value of c="))

if a>b:
    if a>c:
        print("a is greater......")
    else:
        print("c is greater......")
else:
    if b>a:
        print("b is greater .....")
    else:
        print("c is greater......")

'''

#--------------------------------------------------------------------------------------------------------------------------


'''
Q > W.A.P to show use of while loop.

i=1
while i<=6:
    print(i)
    i+=1
    
'''

#----------------------------------------------------------------------------------------------------
'''
Q > W.A.P to display the value from 1 to 10 .

i=1
while i<=10:
    print(i,end=" ")
    i+=1

'''

#-----------------------------------------------------------------------------------------------

'''
Q > W.A.P to display the value from 10 to 1 .

i=10

while i>=1:
    print(i,end=" ")
    i-=1

'''

#-----------------------------------------------------------------------------------------------------------------------

'''
Q > W.A.P infinite loop  in while .

i=1
while i<2:
    print(i)

'''


#============================================================================================================================


'''
Q > W.A.P use of while with else.

case 1:
----------

i=1
while i<=5:
    print(i)
    i+=1
else:
    print("while loop is closed....")

'''

'''
case 2:-
-----------------
i=1
while i<=5:
    print(i)
    i+=1
    if i==3:
        print("hello")

'''

#=============================================================================================================================

'''
Q > W.A.P using for-in loop.
for i in "hello":
#    print(i)
    print(i,end=" ")


'''

#============================================================================================================================

'''
Q > W.A.P  to find no. of vowels present in your name .


name=str(input("Please enter your name = "))
vowel="aeiouAEIOU"
c=0
for i in name:
    if vowel in name:
        c=c+1
        print(name,"contain",c," vowels")

'''


#==============================================================================================================================

'''
Q > W.A.P to display your name 10 times.



name=str(input("enter your name "))

for i in range(10):
    print(name)
    
'''

#==============================================================================================================================

'''
Q > W.A.P to display all even number between 1 - 100 .using for in loop.

x=int(input("enter the range = "))
for i in range(2,x,2):
    print(i,end=" ")

'''

#=============================================================================================================================

'''
Q > W.A.P to display sum of each element from 1 to n.

x=int(input("enter the range= "))
sum=0
for i in range(1,x+1):
    sum+=i
    print(sum)

'''

#=============================================================================================================================

'''
Q > W.A.P to find the factorial of a number by using for in loop.


n=int(input("enter the number= "))

fact=1
for i in range(1,n+1):
    fact=fact*i
    print(fact)
    #enter the number= 5
     #               1
    #              2
     #               6
     #               24
      #              120
    

    #OR

print(fact) # 120

'''

#----------------------------------------------------------------------------------------------------------------------------

'''
Q > W.A.P TO CHECK a no. is prime or composite.


n=int(input("enter the number to check ="))
p=0
for i in range(2,n):
    if n%i==0:
        p=p+1
        if p==2:
            print(n,"is prime")

        else:
            print(n,"not prime")



n=int(input("enter the number = "))
p=0
for i in range(2,n):
    if n%i!=0:
        p+=1
        if p==2:
            print("prime")
            break
    else:
        print("not prime")

'''


#++++++++++========================++++++++++++++++++++++++===================================================================

'''
Q >W.A.P to show use of "break".


for i in "hello":
    if i=="l":
        break
    print(i)

'''

#==============================================================================================================================

'''
Q > W.A.P TO Show the use of 'continue'. 


for i in "hello":
    if i=='l':
        continue
    print(i)
    
'''

#=============================================================================================================================



