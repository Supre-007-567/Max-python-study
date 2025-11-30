"""
猜数字
"""
import random
if 1:
    right_num = random.randint(1, 10)
    g_times = 0
    print(f"猜数字游戏(right_num={right_num})")
    while True:
        my_num = int(input("请输入1-10的数字\n"))
        g_times += 1
        if my_num > 10:
            print("请输入正确数字")
            continue
        elif my_num < 1:
            print("请输入正确数字")
        if my_num > right_num:
            print("猜大了")
        elif my_num < right_num:
            print("猜小了")
        else:
            print(f"恭喜您仅用{g_times}次猜对了，就是{my_num}")
            break
        if g_times == 5:
            print("次数耗尽")
            break
"""
test
"""
