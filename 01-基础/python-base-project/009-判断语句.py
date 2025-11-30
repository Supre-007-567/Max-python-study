"""
判断语句
"""
# 布尔类型
# result = 10 > 5
# print(f"结果: {result}\n类型: {type(result)}")
#
# while True:
#     my_age = int(input("键入年龄\n"))
#     if my_age < 0:
#         print("请键入正确年龄")
#         break
#     if my_age >= 18:
#         print("成年")
#     else:
#         print("未成年")

"""
if else
"""
while True:
    height = input("请输入您的身高(cm)\n")
    if int(height) > 120:
        print(f"身高{height}cm大于120cm，\n您需要支付10元购买门票\n祝您游玩愉快\n")
    elif int(height) < 120:
        print(f"身高{height}cm小于120cm，可以免费畅玩\n祝您游玩愉快\n")
    else:
        print("请输入正确身高")

