# หาจำนวนตัวอักษรพิมพ์เล็กพิมพ์ใหญ่
def checkstring(messege):
    result ={"UPPER":0,"LOWER":0}
    for c in messege:
        if c.isupper():
            result["UPPER"]+=1
        elif c.islower():
            result["LOWER"]+=1
        else:
            pass
    print(result)
checkstring("ABcDef")


