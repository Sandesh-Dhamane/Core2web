'''
#1
a=int(input("Enter the value A : "))
b=int(input("Enter the value B : "))
if(a>b):
    print(a,"is greater than",b)
else:
    print(a,"is less than",b)
'''


'''
#2
a=int(input("Enter the value A : "))
if(a>0):
        print(a,"is positive number")
elif(a==0):
      print(a,"is zero")
else:
    print(a,"is negative number")
'''


'''
#3
a=int(input("Enter the value A : "))
if(a%2==0):
    print(a,"is even")
else:
    print(a,"is odd")
'''


'''
#4
a=int(input("Enter the value A : "))
if(a%5==0):
    print(a,"is divisible by 5")
else:
    print(a,"is not divisible by 5")
'''


'''
#5
a=int(input("Enter the value A in 0 to 6 : "))
if(a==0):
    print("Monday")
elif(a==1):
    print("Tuesday")
elif(a==2):
    print("Wednesday")
elif(a==3):
    print("Thursday")
elif(a==4):
    print("Friday")
elif(a==5):
    print("Friday")
elif(a==6):
    print("Saturday")
else:
    print("Not in the week")    
'''


'''
#6
a = input("Enter a alphabet : ")
if chr(a>=chr(65)): 
     print(a,"is a character")
'''


'''
#7
a = int(input("Enter number of month :"))
if(a==1 or a==3 or a==5  or a==7 or a==8 or a==10 or a==12):
    print("you entered a month with 31 days")
elif(  a== 4 or a== 6 or a==9 or a==11):
    print("You have entered a month with 30 days")
elif(a==2):
    print("28 or 29 days in month")
else:
    print("enter a valid number between 1 to 12")
'''


'''
#8
a=int(input("Enter the value A : "))
if(a>10):
    print("Yes",a,"is greater than 10")
else:
    print("No",a,"is less than 10")
'''


'''
#9
a=input("Enter the alphabet : ")
if(a=='a'or a=='e'or a=='i'or a=='o'or a=='u' or a=='A'or a=='E'or a=='I'or a=='O'or a=='U'):
    print(a,"is vowel")
else:
    print(a,"is a consonant")
'''


'''
#10
a=int(input("Enter the year: "))
if(a%4==0):
    print(a,",yes it is a leap year")
else:
    print(a,",no it is not leap year")

'''