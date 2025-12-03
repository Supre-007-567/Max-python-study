"""
函数
"""


if 0:
    def my_fun(var=None):
        if var is None:
            print("var 传入了 None")
            return
        print("python函数学习")
        print(f"{var}")


    my_fun("彭于晏")
    my_fun()
    my_fun('')
    print(1)


def verify(temp):
    if temp >= 37.5:
        print("请尽快就医")
    else:
        print("欢迎光临")


verify(36)
verify(38)


