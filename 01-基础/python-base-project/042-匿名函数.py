"""
匿名函数
 作为函数参数
"""


def my_fun(computed):
    result = computed(1, 2)
    print(f"my_fun：\nresult={result}")


def computed(num1=10, num2=20):
    """
    :param num1: number1
    :param num2: number2
    :return: num1+num2
    """
    print("computed was executed")
    return num1 + num2


my_fun(computed)

my_fun(lambda x, y: x+y)



