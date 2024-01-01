'''WAP program to calculate and print the product of the count of odd numbers within a given range.
input : start=1,stop=11'''

a=int(input("start :"))
b=int(input("stop :"))

odd_count = 0
product = 1
for number in range(a, b):
    if number % 2 != 0:
        odd_count += 1
        product *= number

print("The count of odd numbers in the range :",(odd_count))
print("The product of odd numbers in the range :",(product))