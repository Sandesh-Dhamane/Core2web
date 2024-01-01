'''
Take two numbers from users and print the sum of those numbers
if the sum is even
'''
num1=int(input("enter the number1 :"))
num2=int(input("enter the number2 :"))
sum=num1+num2
print("sum of two numbers is",sum)
if sum%2 ==0:
    print("sum is even")
else:
    print("sum is odd")