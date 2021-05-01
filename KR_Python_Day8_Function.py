# Function ความสามารถของตัวโปรแกรม
# เป็นโปรแกรมย่อยที่ทำงานอยู่ในโปรแกรมหลัก  รวมคำสั่ง ลดการใช้พื้นที่หน่วยความจำ
# เลือกเรียกใช้ฟังก์ชั่นได้เลย , ชื่อฟังก์ชั่นไม่สามารถใช้ซ้ำกันได้
'''
เพื่อทำให้ไม่ต้องเขียนชุดคำสั่งเดิม ๆ หลายครั้ง
และช่วยให้การเขียนคำสั่งที่มีความซับซ้อนมีประสิทธิภาพมากขึ้น
และมักจะนำการเขียนฟังก์ชันไปใช้กับการหาคำตอบของคำนวณเพื่อหาค่า
หรือลักษณะของงานที่มีการเรียกใช้งานบ่อย ๆ
'''

# --------------- สาเหตุที่ต้องเขียนฟังก์ชั่น

# ปัญหา : มีการใช้คำสั่งที่ซ้ำกันหลายจุดมากๆ
# a,b,c = 12,23,40
#
# if a%2 == 0:
#     print(a ," is Even")
# else:
#     print(a,"is Odd")
# if b%2 == 0:
#     print(b," is Even")
# else:
#     print(b,"is Odd")
# if c%2 == 0:
#     print(c,"is Even")
# else:
#     print(c,"is Odd")

#ลองทำเฉยๆ

# Method 1
# num = [10,23,40]
# for i in num:
#     if i%2 == 0:
#         print(i , "is even")
#     else:
#         print(i, "is odd")

# Method 2
# Structure : ค่าเมื่อเป็นจริง if เงื่อนไข else ค่าเมื่อเป็นเท็จ
# num = [10,23,40]
# for i in num:
#     print(i, "is even") if i%2 == 0 else print(i, "is odd")

# Method 3
# Structure : [c for c in 'word']
# [print(i, "is even") if i%2 == 0 else print(i, "is odd") for i in num]

#-----------------การสร้างฟังก์ชั่นและการเรียกใช้งานฟังก์ชัน

''' Structure ----  def function_name():
                       statement
'''

# การสร้าง
def sayHi():
    print("Hello Function")
def sayThailand():
    print("สวัสดี")

# โปรแกรมหลัก ใช้เรียกฟังก์ชันออกมาทำงาน
sayHi()
sayThailand()
