# เกมทายลูกเต๋า
import random   # ฟังก์ชั่นสุ่มตัวเลข
myrandom = random.randrange(1,7) # 1,6
for i in range(0,3):
    guess = int(input("Please input your number (1-6) : "))
    correct = (guess==myrandom) # true/false
    if correct:
        print("You're correct!")
        break
    else:
        print("You're wrong!")
    i+=1
print("Stop")
print("Ans = ", myrandom)
