'''WAP to print the number divisible by 7 but not divisible by 3 between 1 to 100
input : start :1,stop :100'''

a=int(input("start :"))
b=int(input("stop :"))
for i in range (a,b):
    if i%7==0 and i%3:
        print(i)