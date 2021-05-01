money = int(input('Input your money : '))

if money >= 1000:
    print(money // 1000)
    money = money % 1000
if money >= 500:
    print(money // 500)
    money %= 500
if money >= 100:
    print(money // 100)

