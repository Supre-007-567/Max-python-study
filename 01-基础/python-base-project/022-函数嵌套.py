"""
函数的嵌套
"""


def add(a, b):
    """
    add 两个整数之和
    :param a: 第一个整数
    :param b: 第二个整数
    :return: 两数之和
    """
    return a + b


def fun1():
    num1 = int(input("请输入第一个整数"))
    num2 = int(input("请输入第二个整数"))
    print(f"num1 + num2 = {add(num1, num2)}")


fun1()




