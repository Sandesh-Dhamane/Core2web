'''WAP to print the count of all negative numbers from a given range
input : start=-15,stop=50'''

a=int(input("start :"))
b=int(input("stop :"))
n_count = 0

for i in range (a,b):
    if i < 0:
        n_count +=  1
print ("total count of negative numbers :",n_count)
