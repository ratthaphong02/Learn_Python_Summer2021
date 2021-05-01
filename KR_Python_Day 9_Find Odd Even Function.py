# ฟังก์ชั่นการเลขคี่ - คู่
# Method 1
def oddevenfn(a,b,c):
    for i in a,b,c:
        if i%2 == 0:
            print(i, "is even")
        else:
            print(i,"is odd")
# a,b,c = 10,13,40
# oddevenfn(a,b,c)

def searchnumber(number):
    if number % 2 == 0:
        print(number,"is even")
    else:
        print(number,"is odd")
a,b,c,d = 10,23,40,50
searchnumber(a)
