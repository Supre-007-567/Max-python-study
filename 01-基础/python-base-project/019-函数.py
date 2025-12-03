"""
函数
    组织好的 可复用的 用来实现特定功能的代码段
"""

# 需求：统计字符串的长度 不适用内置函数len()
str1 = '彭于晏'
str2 = '胡歌'
str3 = 'python'


# length = 0
# for item in str3:
#     length += 1
# print(f"strx.length={length}")

def my_len(data):
    count = 0
    for item in data:
        count += 1
    return count


print(f"{str1}的长度是：{my_len(str1)}")
print(f"{str2}的长度是：{my_len(str2)}")
print(f"{str3}的长度是：{my_len(str3)}")
