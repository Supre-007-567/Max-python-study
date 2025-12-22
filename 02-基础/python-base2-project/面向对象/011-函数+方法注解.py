"""
函数+方法 注解
"""


def add_fun(x: int, y: int) -> int:
    return x + y


result = add_fun(1, 2)
print(result)


def func(data: list) -> list:
    for item in data:
        print(item)
    return data
