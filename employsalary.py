''' Q > An employ basic salary  input from keyboard, if the basic salary is greater then  $10000 then DA is 80% ,HR is 60%.
Otherwise DA is 60% and HRA is 40% .find the total salary of employ.'''

sal=int(input("enter the basic salary ="))

if sal>10000:
    da=80/100*sal
    hra=60/100*sal
else:
    da=60/100*sal
    hra=40/100*sal

total=sal+da+hra
print("basic salary is =",sal)
print("total salary = ",total)