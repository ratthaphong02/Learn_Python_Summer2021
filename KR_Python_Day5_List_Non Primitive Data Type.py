#-------------เจาะลึกการใช้ List ----------------#

# Non primitive data type การจัดการข้อมูลเป็นชุด (ใช้เก็บตำแหน่งของข้อมูล)

# non primitive


#------------- 1.นิยาม list--------------#

# number = [] # list ว่าง list สามารถเก็บได้ทั้งตัวเลข, ข้อมูลทางตรรกศาสตร์และตัวอักษรหลายๆตัวได้
number = [1,2,3,4,5,6]
print(number)   # Ans = [1 ,2, 3, 4, 5, 6]

# รูปแบบ constructor
number1 = list([1,2,3,4,5,6])

#-------------2.การเข้าถึงข้อมูล--------------#
print(number[0])  # Ans = 1
print(number[1:3]) # Ans = [2,3]
print(number[:3]) # Ans = [1,2,3]
print(number[2:]) # Ans = [3,4,5,6]
print(number[-1]) # Ans = 6
print(number[-2:]) # Ans = [5,6]
print(number[:-2]) # Ans = [1,2,3,4]
print(number[-3:-1]) # Ans = [4,5]

#-------------4. การแก้ไขข้อมูล-----------#
  # ชื่อlist[index] = "ข้อมูลที่ต้องการแก้ไข"
number[5] = 99
print(number) # Ans = [1, 2, 3, 4, 5, 99]

#-------------5. การแสดงผลด้วย loop -----------#
sum1 = 0
for x in number:
    print(x) # Ans = 1 2 3 4 5 99
    sum1+=x
print(sum1)   # Ans = 114

#-------------6. การตรวจสอบข้อมูล ---------------#

number2 = [1,2,3,4,5,6]

if 10 in number2:
    print("True")
else:
    print("False")

#-------------7. การนับจำนวนสมาชิกโดย len ---------------#

print(len(number2)) # Ans = 6

for i in range(len(number2)):
    print(number2[i])
    i+=1
''' 
Ans =
1
2
3
4
5
6

'''

#-------------8. การเพิ่มข้อมูลด้วย  append , insert ---------------#
   # append  เอาข้อมูลมาต่อท้าย append() takes exactly one argument
   # insert  การเพิ่มข้อมูลแบบแทรกเข้าไป **** insert(index,สมาชิกใหม่)
number2.append(7)
print(number2) # Ans = [1, 2, 3, 4, 5, 6, 7]
number2.insert(3,99)
print(number2) # Ans = [1, 2, 3, 99, 4, 5, 6, 7]

#-------------9. การลบข้อมูลด้วย  remove, pop, del, clear ---------------#

# remove  : listname.remove(สมาชิกที่ต้องการลบ) เป็นการลบโดยระบุสมาชิก

number3 = [1,2,3,4,5,6]

number3.remove(6)
print(number3) # Ans = [1,2,3,4,5]

# pop การลบสมาชิกตัวหลังสุด listname.pop()

number3.pop()
print(number3) # Ans = [1,2,3,4]

# del เป็นการลบโดยระบุ index del list.name[index ที่ต้องการลบ]

del number3[3]
print(number3) # Ans = [1,2,3]

# del แบบเคลียร์หน่วยความจำ หรือลบตัวแปรทิ้งไปเลย

del number3
 # Ans = name 'number3' is not defined เพราะ  number 3 ถูกลบไปแล้ว

# clear ทำให้ list กลายเป็น list ว่าง /

number4 = [1,2,3,4,5,6]

number4.clear()
print(number4) # Ans = []

#-------------10. การคัดลอกข้อมูลด้วย  ---------------#
 # Structure : list ที่จะ paste ข้อมูล = list ที่คัดลอก.copy()
num5 = [1,2,3,4,5]
num6 = []
num6 = num5.copy()
print(num6)

#-------------11. การรวมข้อมูล  ---------------#

num7 = [1,2,3,4,5]
num8 = [6,7,8,9,10]
allg = num7 + num8
print(allg) # Ans = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

 #อีกหนึ่งวิธี
num7.extend(num8)
print(num7) # Ans = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#-------------11. การนับจำนวนสมาชิกใน list  ---------------#

# Structure : listname.count(สมาชิกที่อยากนับใน list)
num9 = [1,3,3,5,3]
print(num9.count(3)) # Ans = 3 เพราะ 3 มี 3 ตัว




