# dictionary เป็นการรวมความสามารถของ list tuple และ set มาอยู่ด้วยกัน
# dictionary สามารถออกแบบ index เองได้ ไม่จำเป็นต้องเป็นจำนวนเต็ม

# list , tuple

lis = [1,2,3]
tup = (1,2,3)
print(lis , lis[0])
print(tup, tup[0])

# --------------------dictionary
# ประกอบด้วย : key เอาไว้อ้างอิงข้อมูล(การเข้าถึงข้อมูล) , value คือส่วนของข้อมูล(ค่าของข้อมูล)

#--------------------- การสร้าง dictionary
# Structure : dict_name = {key1:value1, key2: value2,.....} or dict_name = dict(key1=value1, key2=value2,....)
name = {"R":"Ronaldo", "M":"Messi"}
print(name["M"])
name1 = dict(o="one",t="two")
print(name1["o"])
print(name1.get("o"))  # แสดงผล dict แบบที่ 2

#----------------- การแก้ไขข้อมูล ใน dictionary
# Structure = dict_name[key ที่่ต้องการแก้ไข] = ข้อมูลที่เราต้องการเอาไปแทนที่
name["R"] = "Robert Lewandovski"
print(name)

#----------------- การเพิ่มข้อมูล ใน dictionary
# Structure : dict_name.update({key1:value1,key2:value2,.....})
name.update({"M":"Mbappe"})  # ถ้าเจอคีย์ ไม่ซ้ำจะเพิ่มข้อมูลเข้าไป แต่ถ้าเจอคีย์ซ้ำ จะอัพเดทข้อมูลใหม่
    # Ans =  {'R': 'Robert Lewandovski', 'M': 'Mbappe'}
print(name)

# --------------- การวน loop
# Method 1
# for i in name:
#     print(i) # จะได้ key มาใช้งาน
#     print(name[i])
# Method 2 : อยากได้แค่ key
# for i in name.keys():
#     print(i)
# Method 3 : อยากได้แค่ value
# for i in name.values():
#     print(i)
# Method 4 : อยากได้ทั้ง key และ value
for k,v in name.items():   # ตัวแปร k จะแสดง key ตัวแปร v จะแสดง value
    print(k , v)

# --------------- การลบข้อมูลออกจาก dictionary
# Structure : dict_name.pop(key ของข้อมูลที่ต้องการลบ)
name.pop("R")
print(name)

# Structure : dict_name.popitem()  เป็นการลบข้อมูลที่อยู่ท้ายสุดออกไป
name.update({"A":"Alen Halilovic"})
print(name)
name.popitem()
print(name)

# Structure : dict_name.clear() เป็นการลบสมาชิกใน dict ออกไปให้หมด
name.clear()
print(name)

# Structure : del dict_name คือ การลบตัวแปรนั้นออกจาก project ของเราออกไปเลย
# del name1
# print(name1)

# ------------------- การคัดลอกข้อมูลลงใน dictionary

name2 = {"M":"Mbappe"}
# print(type(name2))
name = name2.copy()  # คัดลอก name2 ไป name
print(name)


#------------------- nested dictionary : การทำ dictionary ซ้อนกัน

prem = {
    "A":"Arsenal",
    "B":"Brighton",
    "L":"Liverpool"
}

# nested dictionary

league = {
    "laliga":{
        "team":"Barcelona",
        "footballer": ["Messi","Pedri"] ,      # ข้อมูลที่เป็น list
        "position":"Forward"
    },
    "premier league":{
        "team":"Liverpool",
        "footballer": ["Salah","Mane"] ,      # ข้อมูลที่เป็น list
        "position":"Forward"
    },
    "bundesliga":{
        "team":"Dortmund",
        "footballer": ["Halland","Sancho"] ,      # ข้อมูลที่เป็น list
        "position":"Forward"
    }

}

print(league["premier league"])


