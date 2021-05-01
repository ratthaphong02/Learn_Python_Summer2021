# Global Variable ตัวแปรของโปรแกรมหลัก ทำงานทั่วโปรแกรม / Local Variable ทำงานเฉพาะส่วนนั้นๆ

def displaynumber():
    # statement
    x = 10
    print(x)

#โปรแกรมหลัก
x = 20   # global x นอก
displaynumber()  # local x ใน
print(x)
