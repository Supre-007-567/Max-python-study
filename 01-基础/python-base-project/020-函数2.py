"""
函数
"""


def my_fun(var=None):
    if var is None:
        print("var 传入了 None")
        return
    print("python函数学习")
    print(f"{var}")


def welcome():
    print("欢迎来到中牟县\n这里是我的故乡")


welcome()


my_fun("彭于晏")
