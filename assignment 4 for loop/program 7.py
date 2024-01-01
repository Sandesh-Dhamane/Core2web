'''WAP that prints all Positive numbers from a given range.
input : start :-7,stop :8'''

a=int(input("start :"))
b=int(input("stop :"))
for i in range (a,b):
    if i>=0:
        print(i)