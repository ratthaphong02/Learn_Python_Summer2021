# สมาชิกที่อยู่ใน set จะไม่มีข้อมูลที่ซ้ำกัน
'''
List = [] ข้อมูลต่างชนิดกัน , แก้ไขสมาชิกข้อมูลได้ , ข้อมูลซ้ำกันได้ ซ้ายไปขวา
Tuple = () ข้อมูลต่างชนิดกัน , แก้ไขสมาชิกข้อมูลไม่ได้ , ข้อมูลซ้ำกันได้ ซ้ายไปขวา
Set = {} ข้อมูลต่างชนิดกัน , แก้ไขสมาชิกข้อมูลได้ , ข้อมูลซ้ำกันไม่ได้ ลำดับข้อมูลไม่แน่นอน
การค้นหาข้อมูลสมาชิก ของ set จะทำได้เร็วกว่า เพราะ ไม่ต้องพิจารณา index
'''
#---------- 1. นิยาม ----------#
# num = {1,2,3,4,5}
# print(num , type(num))
#
#constructor
# num1 = set([1,2,2,3,4])
# print(num1)
#
# #----------2. เพิ่มข้อมูลสมาชิก ------#
# # เพิ่มทีละตัว
# # Structure : set_name.add(สมาชิกที่ต้องการเพิ่มเข้าไป)
# num1.add(5)
# print(num1)
#
# #เพิ่มทีละหลายตัว
# #Model 1
# lis = [6,7,8]
# num1.update(lis)
# print(num1)
#
# #----------3. แสดงผลด้วย loop ------#
# for i in num1:
#     print(i)
#
# #----------4. แสดงจำนวนสมาชิกด้วย len() ------#
# print(len(num1))
#
# #----------5. เช็คสมาชิกใน set -----------#
#
# if 1 in num1:
#     print("Y")
# else:
#     print("N")
#
# #---------6. การลบข้อมูลในสมาชิก -----------#
#
# num1.remove(8)   # remove ถ้าไม่เจอข้อมูล จะเกิด error
# print(num1)
#
# num1.discard(9)   # discard ถ้าไม่เจอข้อมูล จะไม่เกิด error
# print(num1)
#
# num1.clear()      # clear เป็นการลบสมาชิกออกทั้งหมด
# print(num1)
# del num1          # del เป็นการลบตัวแปรนั้นออกไปเลย

#---------7. Set Operator ***** -----------#

set1 = {1,2,3,5}
set2 = {1,2,3,5,6,7,8,9,10}

# ---------union
# Structure : set1.union(set2)
# Method 1
# print(set1.union(set2))
# Method 2
# set1.update(set2)
# print(set1)
# Method 3
# set1 = set2.copy()
# print(set1)

#---------difference พิจารณาว่า มีสมาชิกตัวไหนบ้างที่ไม่เหมือนกัน

print(set2.difference(set1))  # หมายถึง สมาชิกตัวไหนบ้าง ใน set2 ที่แตกต่างจาก set 1  Ans = {6, 7, 8, 9, 10}
print(set1.difference(set2))  # หมายถึง สมาชิกตัวไหนบ้าง ใน set1 ที่แตกต่างจาก set 2 Ans = set()

#--------- intersection

print(set1.intersection(set2)) # Ans = {1, 2, 3, 5}

#--------- Subset เช็คว่า set1 เป็น subset ของ set2 ไหม ?
print(set1.issubset(set2))
print(set2.issubset(set1))

# ------ Superset เช็คว่า set 1 เป็นเซตหลักของ set 2 ได้หรือเปล่า?
print(set1.issuperset(set2))
print(set2.issuperset(set1))

#-------- หาค่า max min ใน set

number = {2,1,9,10,5,99}
print(min(number))
print(max(number))

# ------------------ Frozenset set ที่แก้ไขอะไรไม่ได้เลย ลบไม่ได้ แสดงผลก็ไม่ได้
number1 = frozenset([2,1,9,10,5,99])





