# Default Parameter = คือการกำหนดค่าเริ่มต้นของ parameter

def displaydata(fname,lname,city="Buanos"):
    print(fname)
    print(lname)
    print(city)
# displaydata("Lionel","Messi","Barcelona")
# Keyword Arguments *********
displaydata( lname="Messi",fname="Lionel")
'''
Ans =
Lionel
Messi
Buanos

'''
displaydata("Lionel","Messi","Barcelona") # ถ้าป้อนค่าลงไปด้วย ค่า parameter ในฟังก์ชั่นจะเปลี่ยนไป

'''
Ans =

Lionel
Messi
Barcelona

'''

