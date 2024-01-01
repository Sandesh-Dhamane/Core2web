'''Write a Program to print all Even numbers from a given range.
input : start :10,stop :20'''

a=int(input("start :"))
b=int(input("stop :"))
for i in range(a,b):
    if i%2 ==0:
        print(i)