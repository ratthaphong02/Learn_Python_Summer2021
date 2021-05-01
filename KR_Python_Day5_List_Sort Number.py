# ----------------assignment1 รับและเรียงลำดับตัวเลข-----------------#
# list มีฟังก์ชั่นที่ใช้เรียงลำดับตัวเลข

'''
# Method 1
print("Method 1")
n = int(input("Input Number : "))
number = []
for i in range(n):
    x = int(input("Input your number : "))
    number.insert(i,x)
print(number)
number.sort() # เรียงจากน้อยไปมาก
print(number)
number.reverse() # เรียงจากมากไปน้อย
print(number)

# Method 2
print("Method 2")
number1 = []
while True:
    x1 = int(input("Input your number : "))
    if x1 < 0:
        break
    number1.append(x1)
print(number1)
number1.sort()  # เรียงจากน้อยไปมาก
print(number1)
number1.reverse() # เรียงจากมากไปน้อย
print(number1)
'''

# ----------------assignment2 การหาค่าต่ำสุด-สูงสุด-----------------#
'''
print("Method 1")
number3 = []
max3 = 0
min3 = 10000
while True:
    x3 = int(input("Input your number : "))
    if x3 < 0:
        break
    if x3 > max3:
        max3 = x3
    if x3 < min3:
        min3 = x3
print(max3,min3)


print("Method 2")
number4 = []
while True:
    x4 = int(input("Input your number : "))
    if x4 < 0:
        break
    number4.append(x4)
print("min = ", min(number4))
print("max = ", max(number4))
print("sum = ", sum(number4))  # ผลรวมของสมาชิกใน list
'''

#-------------assignment3 การหากลุ่มเลขคู่-คี่-----------------#
'''
number5 = []
odd = []
even = []
while True:
    x5 = int(input("input your number : "))
    if x5 < 0:
        break
    if x5 % 2 != 0:
        odd.append(x5)
    else:
        even.append(x5)
print(odd)
print(even)

'''

#-------------assignment4 การเรียงลำดับชื่อ-----------------#
'''
name = ["Ronaldo", "Messi", "Alaba"]
name.sort()
print(name)
name.reverse()
print(name)
'''

#-------------assignment5 การเรียงสมาชิกจากหลังไปหน้า-----------------#


'''
fruit = ["มะม่วง", "มะยม", "มะนาว"]
fruit = fruit[::-1]
print(fruit)
'''

#-------------assignment6 หาค่าเลขยกกำลัง -----------------#
'''
print("Method 1")
number = [1,2,3,4,5]
number1 = []
for i in range(len(number)):
    n = number[i]**2
    number1.append(n)
print(number1)

print("Method 2")
for j in range(len(number)):
    number[j] = number[j]*number[j]
print(number)

print("Method 3************")
number = [1,2,3,4,5]
number = [x*x for x in number]
print(number)
'''

#-------------assignment7 การจับคู่สินค้าและราคา -----------------#
'''
name = ["A","B","C"]
num = [1,2,3]
#num[::-1] # เรียงข้อมูลจากท้ายไปหน้า
for i,j in zip(name,num[::-1]):
    print(i,j)
'''

#-------------assignment8 จับคู่คำทักทาย/ บุคคล -----------------#

# greeting = ["Hi","Hello", "Good Morning"]
# people = ["A","B","C"]
# # Method 1
# for i in greeting:
#     for j in people:
#         print(i,j)
# # Method 2
#
# result = []
# for i in greeting:
#     for j in people:
#         result.append(i+j) # เป็นการรวมข้อมูล ของ list
# print(result)
#
# # Method 3 ********************
# result1 = [ x+y for x in greeting for y in people]
# print(result1)

#-------------assignment9 การค้นหาตัวอักษรในสมาชิก -----------------#

# # Method 1
# char = ["AAAB", "CCCB", "ACBB","CAAAACB"]
# cnt = 0
# result = []
# for i in char:
#     result.append(i.count("B"))
#     cnt+=i.count("B")
# print(result)
# print(cnt)


