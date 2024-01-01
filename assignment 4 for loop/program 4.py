'''WAP to print all the character values of the given ASCII value range from the user'''

a=int(input("start :"))
b=int(input("stop :"))

for i in range(a,b):
    character = chr(i)
    print("ascii value for",i,"is",character)