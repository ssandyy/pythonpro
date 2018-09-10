print("enter your name..")
name=input()
vowel="aeiouAEIOU"
c=0
for i in name:
    if i in vowel:
        c=c+1

        
print(name,"contain",c,"vowel")
