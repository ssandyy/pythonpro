# Q > find all prime(divisible by 1 and itself) number from 1 to 100.

for n in range(2,100):
    for i in range(2,n):
        if n%i==0:
            break
    else:
        print(n)