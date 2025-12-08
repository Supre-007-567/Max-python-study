"""
列表是可以被修改的
元组一旦定义完成，就不可修改
元组 = 不可修改的 列表
"""

my_tuple = ("彭于晏", 18, True)
print(f"输出元组{my_tuple}")
print("元组数据类型", type(my_tuple))

print(f"利用下标取出元组中的元素：{my_tuple[0]}")
print("循环")
for item in my_tuple:
    print("遍历元组", item)

print("嵌套元组")
my_tuple2 = ((1, 2, 3, 4), (5, 6, 7))
# print(len(my_tuple2))
for item in my_tuple2:
    print(len(item))
    if len(item) > 1:
        for obj in item:
            print(f"子：{obj}")
    print(f"父：{item}")

