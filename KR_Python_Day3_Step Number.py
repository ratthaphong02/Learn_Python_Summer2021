#ตัวเลขขั้นบันได

'''
input 4

1
12
123
1234

'''

n = int(input("Input your number : "))

for row in range(1,n+1):
    for column in range(1,row+1):
        print("*",end='')    # end=''  คือ การแสดงผลในแนวนอน
    print(" ")



