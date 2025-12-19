"""
自定义模块1
"""

__all__ = ["testA"]


def testA(num1=0, num2=0):
    return num1+num2


def testB(num1=0, num2=0):
    return num1-num2


if __name__ == '__main__':
    print(f"module1: {testA(1, 2)}")

