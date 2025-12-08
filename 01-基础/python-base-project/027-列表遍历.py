"""
while 遍历列表
"""
users_info = [{"username": "彭于晏", "age": 18}, {"username": "胡歌", "age": 20}]
length1 = len(users_info)
print("while循环")
i = 0
while i < length1:
    print(f"用户名：{users_info[i]['username']}\t年龄：{users_info[i]['age']}")
    i += 1
"""
for 遍历列表
"""
print("for循环")
for user in users_info:
    print(f"用户名：{user['username']}\t年龄：{user['age']}")

num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_list = []
print("偶数循环")
for item in num_list:
    if item % 2 == 0:
        new_list.append(item)
print(f"循环之后{new_list}")



