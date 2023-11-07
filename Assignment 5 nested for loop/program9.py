'''
1 3 5
3 5 7
5 7 9
'''

num=1
for i in range(3):
    #num=i+1
    for j in range(3):
        print(num,end=" ")
        
        num=num+2
    num=num-4
    print()
