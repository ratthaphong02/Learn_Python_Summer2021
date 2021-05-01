# lambda function or Anonymous Function = สร้าง def ขึ้นมาแบบไม่ระบุชื่อ
'''
Structure : lambda arguments :expression

'''

# x = lambda name: name  # ต้องมีตัวแปรรับค่า
#
# print(x("Book"))

# เขียน lambda ซ้อนฟังก์ชั่น

def mypower(x):
    return lambda a : x**a
y = mypower(5)  # เรียกฟังก์ชั่น mypower
result = y(2)   # y(2)  a = 2  # เรียก y = lambda a: 5**a
print(result)
