
"""
关键字传参
    作用：函数更加清晰，可以不按顺序传
"""


def my_fun(name, age, school="xx大学"):
    print(f"My name is{name}.\tI'm {age} years old.\tI'm studying at {school}")


# my_fun(school="周口师范学院", age=18, name="彭于晏")
# my_fun(name="王富贵", age=18)


"""
    不定长参数(可变参数)：用于不确定调用的时候会传多少个参数(不传也可以)的场景
    作用：当调用函数时不确定参数个数，可以使用不定长参数
"""


def my_fun(*args):
    print(f"args参数的类型是：{type(args)}\n{args}\n\n")


my_fun(1, 2, True, '小明')


def my_fun(**kwargs):
    print(f"args参数的类型是：{type(kwargs)}\n{kwargs}\n\n")


my_fun(name="彭于晏", age=18)


