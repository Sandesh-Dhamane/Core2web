'''Take a number from the user and check whether it is present in the list. If
it's in the list, print "Available."
List1 = [10, 20, 30, 40, 50]
'''
List1 = [10, 20, 30, 40, 50]
number=int(input("enter the number :"))
if number in List1:
    print("available")
else:
    print("not available")