"""

"""
my_list = ["黑马程序员", "传智播客", "黑马程序员", "传智播客", "itheima", "itcast", "itheima", "itcast", "best"]

"""
  定义一个空集合
    通过for循环遍历
    在for循环中将列表的元素添加至集合
    最终得到元素去重后的集合对象，打印输出
"""

my_set = set()

for item in my_list:
    my_set.add(item)

print(f"遍历+add结果：{my_set}")










