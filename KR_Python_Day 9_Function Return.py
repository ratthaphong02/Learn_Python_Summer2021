# ฟังก์ชั่นแบบคืนค่า (return function)
"""
ประเภทฟังก์ชั่น
1. ไม่มีการรับค่าและส่งค่า
def name():

2. มีการส่งค่าเข้าไปทำงาน
def name(a,b):

3.  รับค่าเข้าไปทำงาน และส่งออกมา เพื่อนำไปใช้ที่โปรแกรมหลัก
def name(a,b):
    return a+b

4. ไม่มีการรับค่าเข้ามา แต่ส่งค่าออกไป

"""
# แบบที่ 3.1 return แล้วแสดงผล
def add(a,b):
    return a+b
# print(add(10,20))

# แบบที่ 3.2 return แล้วเก็บในตัวแปร

# x = add(10,20)
# print(x)
#
# #แบบที่ 4.1
#
# def shownumber():
#     return 500
# print("number = ", shownumber())


# def randomnumber(n):
#     import random
#     random1 = random.randrange(1,11)
#     if n == random1:
#         print("You Won!")
#     else:
#         print("You Lost!")
#     return random1
# n = int(input("Input your number : "))
# print("Random is ", randomnumber(n))

def randomnumber(x):
    if len(x) < 3:
        return                       # การใช้ฟังก์ชั่น return กระโดดออกจากการทำงาน
    if x == "100":
        print("Win Prize!")
        return 1000
    else:
        print("Lost Prize!")
        return 0

money = randomnumber(200)
print("Prize = ", money)






