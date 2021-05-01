# คุณสมบัติคล้ายๆกับ list ต่างกันที่ tuple ข้อมูลสมาชิกจะไม่สามารถเปลี่ยนแปลงได้

#------------------ 1. การนิยาม , constructor ---------------------#
''' Structure : tuple_name = (ele1, ele2,....)
                or
                tuple_name = tuple((ele1, ele2,....))
'''

tup = (1,2,3,4,5)  # tuple
tup1 = tuple((1,2,3,4))  # โครงสร้าง tuple แบบ constructor
lis = [1,2,3,4]  # list
lis1 = list([1,2,3,4]) # โครงสร้าง list แบบ constructor
lis2 = list(tup)    # การแปลง tuple เป็น list

# print(tup, type(tup))   # Structure : type(ตัวแปรที่ต้องการทราบชนิดข้อมูล)
# print(tup1, type(tup1))
# print(lis, type(lis))
# print(lis1, type(lis1))
# print(lis2, type(lis2))

#------------------ 2. การเข้าถึงข้อมูล ---------------------#
''' Structure : tuple_name[index ที่ต้องการเข้าถึง]'''
# print(tup[0])
# print(tup[-1])
#------------------ 3. การเข้าถึงข้อมูลแบบกำหนดช่วง ( Slice ) ---------------------#
''' Structure : tuple_name[index1 : จนถึงก่อน index2]'''
# print(tup[0:3])  # แสดงตั้งแต่ index = 1 ถึง index ก่อน 3 (ถึง index = 2)
# print(tup[1:])   # แสดงตั้งแต่ index = 1 ถึง index ตัวสุดท้าย
# print(tup[:2])   # แสดงตั้งแต่ index ก่อน 2 ลงไป
# print(tup[-3:-1]) # แสดงตั้งแต่ ตำแหน่ง index = -3 ถึง index ก่อน -1  (ถึง index = -2)

#------------------ 4. การแก้ไขข้อมูล ---------------------#

''' Method : แปลงเป็น list ก่อน'''
tup = (1,2,3,4,5)
lis2 = list(tup)    # การแปลง tuple เป็น list
lis2[-1] = 99
tup = tuple(lis2)
# print(tup)

#------------------ 5. การแสดงผลด้วย loop ---------------------#

# for i in tup:
#     print(i,end=' ')

#------------------ 6. การตรวจสอบข้อมูล ---------------------#

''' Mean : เป็นการเช็คว่ามีสมาชิกที่เราสนใจ ใน tuple ที่เราสนใจไหม?'''
# if 99 in tup:
#     print("Y")
# else:
#     print("N")

#------------------ 7. นับจำนวนสมาชิก (len) ---------------------#

'''Method : ใช้ len(ตัวแปรที่ต้องการนับจำนวนสมาชิก) / นับว่ามีสมาชิกกี่ตัวในตัวแปรที่เราสนใจ'''
# print(len(tup))


#------------------ 8. len() ทำงานร่วมกับ loop for ---------------------#

# for i in range(len(tup)):
#     print(tup[i],end=" ")

#------------------ 9. การสร้างและเพิ่มข้อมูล (Join) ---------------------#

x = ("A", "B")
y = tuple("C")
x+=y
print(x)

#------------------ 10. การทำงานร่วมกับ list ---------------------#

''' Method : แปลง list เป็น tuple หรือ tuple เป็น list แล้วก็ทำการรวมข้อมูลด้วยการ +'''

#------------------ 11. การลบข้อมูล del , การลบแบบ list ---------------------#

'''Method : แปลง tuple เป็น list แล้วลบแบบ list แล้วก็ค่อยแปลงกลับ'''

#------------------ 12. ค้นหาและนับจำนวนสมาชิก (Count) ---------------------#
""" Structure : tuple_name.count(สมาชิกที่ต้องการนับว่ามีกี่ตัวใน tuple ที่เราสนใจ)"""
#------------------ 13. ค้นหาสมาชิกด้วย index ---------------------#
"""Structure : tuple_name.index(index ที่เราสนใจ)"""

#------------------ 14. การ sort ข้อมูล ---------------------#
"""Method : แปลง tuple ให้เป็น list แล้ว sort แบบ list"""

n = (1,4,8,9,2,10,5,11,7)


#------------------Problems----------------------------#

c = n[0] + n[1]
print(c)

# สลับ tuple
x1 = (50,60)
y1 = (88,99)
x1,y1 = y1,x1
print(x1)
print(y1)

# นำ character มาต่อกัน
name = ("b","o","o","k")
name= "".join(name)
print(name)

# reversed tuple

n1 = reversed(n)
print(tuple(n1))
