"""
字符串格式化
"""
print("--------------%占位-----------------------")
age = 18

my_message = "我叫彭于晏今年 %d 岁" % age

print('message1 = ', my_message)

class_num = 9
stu_id = 2023
my_name = "彭于晏"
my_message = "我叫%s，是%s届软件工程%s班学生" % (my_name, stu_id, class_num)
print('message2 = ', my_message)

my_num = 11.1
# 整数 浮点数 精度
print("浮点数%.2f" % my_num)

print("--------------f快速占位-----------------------")
print(f"我叫{my_name}今年{age: .2f}岁")


print("--------------表达式格式化-----------------------")
print(f"11+11={11 + 11: .2f} ")
print(f"字符串类型: {type('123')}")


















