# ฟังก์ชั่นหาผลรวมและค่าเฉลี่ยตัวเลข

# Method 1
# sum1 = 0
# while True:
#     n = int(input("Input your number : "))
#     if n < 0:
#         break
#     sum1+=n
#     avg = sum1/n
# print(sum1,avg)

# Method 2
# def summation(sum1,i):
#     n = int(input("Input your number : "))
#     if n < 0:
#         avg = sum1/i
#         return sum1, avg
#     else:
#         i+=1
#         return summation(sum1+n,i)
# print(summation(0,0))

# Method 3
# def summation(number):
#     total = 0
#     for i in number:
#         total+=i
#     return total
# x = [1,2,3,4,5]
# y = summation(x)
# print(y)

# Method 4

def summation(number):
    total, avg = 0,0
    for i in range(len(n)):
        total+=number[i]
    return total , total/len(n)
n = [1,2,3,4,5]
x = summation(n)
print(x)
