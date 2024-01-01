'''WAP to print the sum of all numbers from a given range.
input : start :1,stop :10'''

a=int(input("start :"))
b=int(input("stop :"))
num=0
for i in range(a,b):
    num=num+i
    print(num)