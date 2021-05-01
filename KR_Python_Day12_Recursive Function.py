''' Recursive Function = ฟังก์ชั่นที่ใช้เรียกตัวเอง '''


''' def ทั่วไป '''
# def a():
#     print("A")
#     b()
# def b():
#     print("B")

# a()

''' recursive function  = จะทำซ้ำไปเรื่อยๆ ปริ้นซ้ำๆ infinity loop'''
# def a1():
#     print("A")
#     a1()


''' หาจุดวนซ้ำ หาจุดออกจากฟังก์ชั่น ต้องมี parameter'''
'''โจทย์ : อยากได้เลข 1-5 ห้ามใช้ for,while loop ให้ใช้ recursive'''

# def add(number):
#     if number == 6:
#         return
#     print(number)
#     number+=1
#     add(number)
# add(1)

'''โจทย์ : สร้างฟังก์ชั่นบวกเลข'''
# Method 1 :
# def sum(number,s):
#     if number == 11:
#         print(s)
#         return
#     s+=number
#     number+=1
#     sum(number,s)
# sum(1,0)

def summation(number):
    if number == 1:
        return number
    else:
        return number+summation(number-1)
s = summation(5)
print(s)
'''
การทำงานของ summation
5
5 + summation(4)
5 + 4 + summation(3)
'''








