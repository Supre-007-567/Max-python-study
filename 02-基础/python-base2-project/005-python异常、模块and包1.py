"""
python 异常
"""
# 常规异常捕获
# try:
#     f = open("C:/Users/ASUS/Desktop/曲高和寡/02-基础/bug.txt", "r", encoding="UTF-8")
# except:
#     print("出现bug，改为 w")
#     f = open("C:/Users/ASUS/Desktop/曲高和寡/02-基础/bug.txt", "w", encoding="UTF-8")

# 捕获指定异常
# try:
#     # print(name)
#     1 / 0
# except (NameError, ZeroDivisionError) as e:
#     print("异常：变量未定义/除数异常")
#     print(e)


# 捕获所有异常
try:
    # 1 / 0
    # print(name)
    print("python")
except Exception as e:
    print(f"出现异常：\n{e}")
else:
    # 无异常情况
    print("else无异常")
finally:
    print("结束--文件关闭函")
