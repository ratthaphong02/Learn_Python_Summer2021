
# การเข้าถึงตัวอักษร
name = "kongruksiam"  # index ตัวอักษรเริ่มต้นที่ 0 , index รวมถึงช่องว่างด้วย
print(name[0])   # Ans = k
print(name[0:3]) # Ans = kon แสดงผลก่อนถึง index สุดท้าย
print(name[:4]) # ans = kon แสดงตั้งแต่ตำแหน่งเริ่มต้นจนถึงตำแหน่งสุดท้าย
print(name[-2:]) # ans = am
print(name[-4:-2]) # ans = si

# การหาความยาวของ string : len function
print(len(name))

# การลบช่องว่าง ใน string ด้วย strip
name1 = " book "
print(name1)
name1 = name1.strip()  # การลบช่องว่างซ้ายขวา
print(name1)
name2 = " BOOK "
print(len(name2))
name2 = name2.lstrip()  # การลบช่องว่างด้านซ้าย
print(len(name2))

# การแปลง case ของ string

print(name.upper())  # แปลงพิมพ์เล็ก --> พิมพ์ใหญ่
print(name2.lower())  # แปลงพิมพ์ใหญ่ --> พิมพ์เล็ก

print(name2.capitalize())  # การแปลงข้อความให้ตัวแรกเป็นตัวพิมพ์ใหญ่

print(name.replace("kong", "555"))   # การแทนที่ตัวอักษร
                  #ตัวเก่า     #ตัวใหม่ที่มาแทนที่

name3 = "Book 4 4" # การแทนที่ตัวอักษรแบบระบุตำแหน่ง ( count )
print(name3.replace("4","5", 1))  # ans = Book 5 4
                            # เปลี่ยน 4 เป็น 5 ที่ ตามจำนวน count จากซ้ายไปขวา
print(name3.replace("4","5", 2))  # ans = Book 5 5

# การเช็คข้อความ (เช็คว่ามีข้อความนี้อยู่ในประโยคหรือเปล่า) ใช้ in
name4 = " N P K"
print("N" in name4)

x = "N" in name4
if x:
    name4 = name4.replace("N","A")
print(name4)

#--------------------------EP 26 เจาะลึก String ตอนที่ 2 Kongruksiam -----------------------#

''' 1. การต่อ string (concatinate)'''
fname = 'book'
lname = 'pook'
age = '22'
print(fname+'\t'+lname)

''' 2. การจัดรูปแบบการแสดงผล โดยใช้ ฟังก์ชัน format  + {} (ปีกกาเอาไว้แทน string)'''
'''แบบที่ 1'''
text = "nickname :{}\tsurname :{} \tage :{}"
print(text.format(fname,lname,age))
'''แบบที่ 2'''
text2 = "nickname :{0}\tsurname :{1} \tage :{2}"
print(text2.format(fname,lname,age))

''' 3. การนับจำนวนคำในประโยค โดย count'''
fruit = 'orangedurianmangodurian'
print(fruit.count("durian"))

''' 4. การเช็คคำขึ้นต้น ด้วย startswith / คำลงท้าย ด้วย endswith ใช้กับ ifelseได้'''
print(fname.startswith("b"))
print(fname.endswith("n"))







