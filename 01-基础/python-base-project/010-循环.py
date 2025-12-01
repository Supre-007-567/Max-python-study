"""
循环
"""
import random
index = 1
total = 0
# while index < 100:
#     print(index+1)
#     index += 1

# while index <= 100:
#     total += index
#     index += 1
# print(f"1-100累加和：{total}")

"""
while 猜数字
"""
print("猜数字游戏(请猜测1-100之间的整数)\n注意：错误格式不计入猜测次数")
num = random.randint(1, 100)
flag = True
while_times = 0
print(f"num={num}")
# while flag:
#     guess_num = input()
#     if int(guess_num) > 100:
#         print("请输入1-100的整数")
#         continue
#     elif int(guess_num < 1):
#         print("请输入1-100的整数")
#         continue
#     while_times += 1
#     if int(guess_num) > num:
#         print("猜大了")
#     elif int(guess_num < num):
#         print("猜小了")
#     else:
#         flag = False
#         print(f"恭喜您使用了{while_times}次猜对了")
for item in range(num):
    for demo in range(10):
        while_times += 10
    print(f"今年喝了{item+1}次酒")
print(f"花费了{while_times}元")

