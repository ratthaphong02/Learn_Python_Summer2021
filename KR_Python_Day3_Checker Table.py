#สร้างตารางหมากฮอส

n = int(input("Input your number : "))

for i in range(1,n+1):
    for j in range(1,n+1):
        if (i+j)%2 != 0:
            print("x",end='')
        else:
            print("o",end='')
    print(" ")



