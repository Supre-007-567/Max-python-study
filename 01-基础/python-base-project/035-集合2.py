"""
集合的差集
"""

# 取出两个集合的差集
set1 = {1, 5, 6}
set2 = {1, 2, 3}
diff = set1.difference(set2)
print(f"差集结果：{diff}\nset1：{set1}\nset2：{set2}")

# 删除和集合2相同的元素
set1.difference_update(set2)
print(f"set1发生变化：{set1}\nset2不变：{set2}")

# 合并为1个
res = set1.union(set2)
print(f"合并后的结果:{res}")

length = len(res)
print(length)

# 遍历集合
for item in res:
    print(item)






