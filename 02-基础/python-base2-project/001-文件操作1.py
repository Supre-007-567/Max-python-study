"""
文件读取
"""
# 打开(获取)文件
import time

f = open("C:/Users/ASUS/Desktop/曲高和寡/02-基础/file-python-test.txt", "r", encoding="UTF-8")
print(f"typeof(f) = {type(f)}")


# 读文件
# f.read(10)
# print(f"读取10字节的结果：\n{f.read(10)}")
# print(f"读取所有字节的结果：\n{f.read()}")
print("----------------------------")
# readlines 读取文件的全部行 封装到列表中
# lines = f.readlines()
# print(f"按行全部读取{lines}")
# for line in lines:
#     print(line)


# readlines 单行读取
# line1 = f.readline()
# print(f"第一行：{line1}")
# line2 = f.readline()
# print(f"第二行：{line2}")
# line3 = f.readline()
# print(f"第三行：{line3}")

# for line in f:
#     print(f"每一行数据：{line}")
#
# time.sleep(3)
# f.close()

with open("C:/Users/ASUS/Desktop/曲高和寡/02-基础/file-python-test.txt", "r", encoding="UTF-8") as f:
    for line in f:
        print(f"每一行数据{line}")







