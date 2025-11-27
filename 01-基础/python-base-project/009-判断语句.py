"""
判断语句
"""
# 布尔类型
result = 10 > 5
print(f"结果: {result}\n类型: {type(result)}")

while True:
    my_age = int(input("键入年龄\n"))
    if my_age < 0:
        print("请键入正确年龄")
        break
    if my_age >= 18:
        print("成年")
    else:
        print("未成年")


