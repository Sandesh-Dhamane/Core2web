'''WAP to determine whether entered angles define a right-angled triangle.
Take three values of angle from the user.
Input1: angel1 = 90
Input2: angle2 = 90
Input3: angle3 = 90
'''
angle1= int (input("enter the angle :"))
angle2= int (input("enter the angle :"))
angle3= int (input("enter the angle :"))
if angle1+angle2+angle3 ==180:
    print("triangle is right angled triangle")
else:
    print("it is not right angled triangle")