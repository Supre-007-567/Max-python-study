"""
嵌套循环
"""
if 0:
    item = 0
    for item in range(1, 6):
        print(f"第{item}天")
        for obj in range(1, 4):
            print(f"第{obj}顿饭")
    print(f"一共过了{item}天")

"""
for-99乘法表
"""
for i in range(1, 10):
    for j in range(1, i+1):
        print(f"{j}*{i}={j*i}\t", end='')
    print()

