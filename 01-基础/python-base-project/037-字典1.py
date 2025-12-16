"""
字典
"""

score_obj = {"彭于晏": 88, "胡歌": 66, "周星驰": 20}

print(f"集合：{score_obj}\n字典类型：{type(score_obj)}")

# 定义空字典
my_dict = {}
print(f"空字典{my_dict}")

print(f"彭于晏：{score_obj['彭于晏']}")

score_list2 = [
    {"name": "彭于晏", "score": 100},
    {"name": "周星驰", "score": 100},
    {"name": "邱淑贞", "score": 100}
]
print(f"列表字典：{score_list2}")

for item in score_list2:
    print(f"姓名：{item['name']}\t得分：{item['score']}")

score_list2[0]["name"] = "胡歌"
print(f"修改值：{score_list2[0]}")


score_list2[0]["gender"] = "男"
print(f"新增值：{score_list2[0]}")

score_list2[0].pop("score")
print(f"pop后{score_list2[0]}\n\n\n")

"""
遍历字典
"""
# 1.获取全部 key
keys = score_list2[0].keys()
print(f"获取全部键{score_list2[0].keys()}")
# 2.
for key in keys:
    print(score_list2[0][key])

print("\n\n")
for item in score_list2[0]:
    print(item)
    print(score_list2[0][item])


print(len(score_list2[0])) 






