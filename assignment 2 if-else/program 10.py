'''Take the number from user and modulus with 8 if the reminder of the number is 3 then print reminder.'''
num=int(input("enter the number :"))
remainder = num%8
if remainder ==3:
    print(remainder)
else:
    print("remainder is not 3")