#--------------------------EP 28 โครงสร้างควบคุมแบบทำซ้ำ -----------------------#

#--------------While-----------#
'''
while expression :
    statement
'''

#------------ For loop  ใช้เมื่อจำนวนรอบที่ชัดเจน----------#
'''
for i in range(start, stop, step): จะทำงานจนถึงก่อน stop
   statement
'''

#------------ loop ซ้อน loop-----------------------#

for i in range(1,12+1):
    for j in range(1,12+1):
        print(i, "x", j , "=", i*j)
        
