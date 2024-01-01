'''WAP to print all the ASCII values from a given character range.
input : start=A,stop=Z'''

a=input("start :")
b=input("stop :")
a=ord(a)
b=ord(b)
if 65 <= a <= 90 and 65 <= b <= 90:
    for i in range(a, b):
        print("The character of ASCII value", i, "is", chr(i))
else:
    print("Enter correct ASCII values in the range A-Z.")