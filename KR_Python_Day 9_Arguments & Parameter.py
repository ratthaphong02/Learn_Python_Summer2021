
# Arguments => ค่าที่ส่งเข้าไปในฟังก์ชั่น # Arguments = name, lname (ตอนเรียกใช้งานฟังก์ชั่น)
# Parameter => ค่าตัวแปรที่รับข้อมูลที่ส่งมาทำงาน จาก Arguments = a,b
#อาส่ง - พารับ

def mydata(a,b):     # ส่งค่าใน () Structure : def func_name(ตัวแปรที่ต้องการส่งเข้ามาทำงานในฟังก์ชัน(parameter))
    print("name:",a,b)

name = input("Input name: ")
lname = input("Input lname: ")
mydata(name,lname)
