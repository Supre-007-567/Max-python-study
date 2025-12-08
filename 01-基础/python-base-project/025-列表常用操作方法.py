"""
列表 list 常用操作方法
"""
usersInfo = ["彭于晏", "胡歌"]

# 查询指定元素在列表中的下标(如果元素不存在，会报错：'xx' is not in list)
flag = usersInfo.index("胡歌")
print(f"”胡歌“的下标为：{flag}")

# 在指定位置插入新元素 list.insert(下标，元素)
usersInfo.insert(0, "邱淑贞")
print(f"插入列表头部新的值{usersInfo}")
usersInfo.insert(len(usersInfo), "吴镇宇")
print(f"插入列表尾部新的值{usersInfo}")

# 追加元素 - 在列表尾部追加一个元素
usersInfo.append("林青霞")
print(f"追加元素到尾部{usersInfo}")
# 追加一批元素
usersInfo.extend(["567", "007"])
print(f"追加一批元素{usersInfo}")

# 删除 ① del列表[下标]  ② 列表.pop(下标)
usersInfo2 = ["彭于晏", "胡歌", "周星驰", "大B哥", "吴彦祖", "周慧敏", "王祖贤", "张曼玉"]
del usersInfo2[0]
print(f"删除①{usersInfo2}")
usersInfo2.pop((len(usersInfo2)-1))
print(f"删除②{usersInfo2}")
# 通过元素内容删除
usersInfo2.remove("大B哥")
print(f"通过内容删除{usersInfo2}")

# 清空
usersInfo2.clear()
print(f"列表被清空了{usersInfo2}")

# 统计某一个值在列表内的数量
usersInfo3 = ["彭于晏", "邱淑贞", "汤唯", "王源", "彭于晏", "567", "007", "007"]
print(f"“彭于晏”出现了{usersInfo3.count('彭于晏')}次")

