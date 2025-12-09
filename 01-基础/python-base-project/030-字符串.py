"""
以数据容器的视角来看字符串
"""

# 字符串常见操作
my_str = "Supreme007567"
# index 查询特定子串索引
print(f".index={my_str.index('0')}")

# 字符串替换 replace  注：不是修改，而是得到一个新的字符串
str_new = my_str.replace('0', '8')
print(f"替换后的新字符串={str_new}")

"""
    字符串的分割 split 
    按照指定的字符串，将字符串划分为多个字符串，并存入列表对象中
    注：不是修字符串，而是得到一个列表对象
"""
my_str = "Hello python This is SupreCoder007"
# 实参需要传入按什么来切割，这里是按空格
str_new = my_str.split(" ")
print(f"切割后的字符串={str_new}")
str_new = my_str.split("e")
print(f"按'e'切割后的字符串={str_new}")

# 字符串规整操作 strip (去除前后空格)
my_str = "   Hello python  "
print(f"去除前后空格{my_str.strip()}")
# 去除自定字符串(只能去除头和尾)
my_str = "Hello python This is SupreCoder007"
print(f"去除007={my_str.strip('007')}")

# 统计字符串中某字符串的出现次数
my_str = "Hello python This is SupreCoder007"
print(f"e在字符串中出现的次数{my_str.count('e')}")
















