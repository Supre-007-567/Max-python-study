"""
切片
"""
my_arr = [1, 2, 3, 4, 5, 6]
new_arr = my_arr[1: 3: 1]
print(f"切片: {new_arr}")

#  对tuple进行切片，从头开始，到最后结束，步长为1
my_tuple = (0, 1, 2, 3, 4, 5, 6, 7)
# 起始和结束不屑表示从头到尾，步长为1可以省略
new_tuple = my_tuple[:]
print(f"切片后的元组: {new_tuple}")

# 对字符串切片 从头开始 到最后结束 步长为2
my_str = "0123456789"
new_str = my_str[::2]
print(f"切片后的字符串{new_str}")

# 对字符串切片 从头开始 到最后结束 步长为 -1(相当于序列反转)
new_str = my_str[::-1]
print(f"切片后的字符串{new_str}")

# 对列表进行切片 从3开始 到1结束 步长为 -1
my_arr = [1, 2, 3, 4, 5, 6]
new_arr = my_arr[3:1:-1]
print(f"列表倒切: {new_arr}")

# 对元组进行切片 从头开始 到最后结束 步长为 -2
my_tuple = (0, 1, 2, 3, 4, 5, 6, 7)
new_tuple = my_tuple[::-2]
print(f"元组倒切: {new_tuple}")


