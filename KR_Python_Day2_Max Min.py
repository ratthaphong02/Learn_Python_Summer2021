max1, min1 = 0,10000
while True:
    number = float(input("input your number : " ))
    if number < 0:
        break
    if number > max1:
        max1 = number
    if number < min1:
        min1 = number
print(max1, min1)
