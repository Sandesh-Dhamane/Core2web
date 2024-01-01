'''WAP to prints numbers which are divisible by 3 and 5 both in a given range.
input : start=15,stop=50'''

a=int(input("start :"))
b=int(input("stop :"))
for i in range (a,b):
    if i%3 ==0 and i%5 ==0:
        print (i)