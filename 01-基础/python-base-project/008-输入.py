"""
python输入
"""
my_name = input("键入姓名\n")
my_gender = input("键入性别\n")
print('用户名：%s \n性别：%s' % (my_name, my_gender))

# 输入数字类型
my_age = input("键入年龄\n")
print(f"值：{my_age}\n类型：{type(my_age)}")
print(f"值：{int(my_age)}\n类型：{type(int(my_age))}")
