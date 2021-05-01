# ฟังก์ชั่นเรียกฟังก์ชั่น

def equal(x,y,z):
    # a = compare(x,y) # ฟังก์ชั่นเรียกฟังก์ชั่น
    # b = compare(a,z)
    # return b
    return compare(compare(x,y),z)


def compare(x,y):
    if x > y:
        return x
    else:
        return y

print(equal(10,5,20))
