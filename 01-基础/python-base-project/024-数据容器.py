"""
数据容器
  列表
"""
# 一个可以存储多个元素的python数据类型
# list(列表) tuple(元组) str(字符串) dict(字典)

# 定义
usersInfo = ["彭于晏", "胡歌", "周星驰", "谢霆锋"]
# 访问
print(f"userInfo[0]={usersInfo[0]}")
# 修改
usersInfo[0] = "彭yu晏"
# 遍历
for user in usersInfo:
    print(f"用户名: {user}")


