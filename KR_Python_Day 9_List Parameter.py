# List parameter

# def dispfruit(item):
#     print(item)

# def dispfruit(item):
#     for i in item:
#         print(i)

def dispfruit(item):
    for i in range(len(item)):
        print(item[i],end=" ")

fruit = ["A", "B"]
dispfruit(fruit)

# Function สามาส่ง tuple เข้าไปทำงานได้
