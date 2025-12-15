"""
集合-
    a. 自动去重
    b. 无序
"""

my_set = {"彭于晏", "胡歌", "周星驰", "彭于晏", "胡歌", "周星驰", "彭于晏", "胡歌", "周星驰"}
# 空集合
# my_empty_set = set()
# print(f"my_set: {my_set}\nmy_empty_set: {my_empty_set}")

# 添加新元素
my_set.add("邱淑贞")
print(f"为集合添加一个元素(还是无序)：{my_set}")


# 移除一个元素
# my_set.remove("邱淑贞")
# print(f"为集合删除一个元素(还是无序)：{my_set}")

# 随机取出一个元素
item = my_set.pop()
print(f"取出的元素：{item}, 原集合：{my_set}")

# 清空集合
my_set.clear()
print(f"清空后的集合: {my_set}")





