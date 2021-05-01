#สร้างขอบตาราง

n = int(input("input your number : "))

for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1:
            print("o",end='')
        else:
            if j == 0 or j == n-1:
                print("o",end='')
            else:
                print("x",end='')
    print(" ")
