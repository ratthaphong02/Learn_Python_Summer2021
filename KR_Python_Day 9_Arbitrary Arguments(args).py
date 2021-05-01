# Arbitrary Arguments
# Python ชื่อฟังก์ชันซ้ำกันไม่ได้ ยกเว้นจะกำหนด parameter ต่างกัน
# def add(x,y):
#     print(x+y)
# add(20,10)

# การกำหนด parameter มีจำนวนไม่ชัดเจน(กำหนด parameter ไม่จำกัดจำนวน) หรือเรียกว่า parameter ไร้ชื่อ = args
# args[index]  , index = 0,1,2,3,.....

# def add(*args):
#     print(args)
#
# add(10)
# add(10,20)
# '''
# Ans =
# (10,)
# (10, 20)
# ''''

# def add(*args):
#     print(args[0]+args[1])
# add(10,20)

def add(*args):
    sum = 0
    for i in args:
        sum+=i
    print(sum)
add(1,2,3,4,5,6,7,8,9,10)

def add1(*item):    # args เป็น tuple
    sum1 = 0
    for i in range(len(item)):  # ในฟังก์ชั่น range จะต้องเป็นจำนวนเต็ม
        sum1+=item[i]
    print(sum1)
add1(1,2,3,4,5,6,7,8,9,10)

# * ข้างหน้า ตัวแปร จะกลายเป็น parameter ไร้จำกัด
