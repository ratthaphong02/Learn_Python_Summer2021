''' โจทย์ : Fibonacci '''

# Method 1
# def fibonacci(f0,f1):
#     if f0 == 144 and f1 == 233:
#         return
#     else:
#         fn = f0 + f1
#     f0 = f1
#     print(fn,end=" ")
#     fibonacci(f0,fn)
# fibonacci(0,1)

# Method 2

# 0,1,1,2,3,5,8,....
def fibonacci(number):
    if number <=1:
        return number
    else:
        return fibonacci(number-1) + fibonacci(number-2)
for i in range(5):
    print(fibonacci(i),end=" ")
