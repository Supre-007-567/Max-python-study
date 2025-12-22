"""
变量类型注解
"""
import json
import random

my_name: str = '彭于晏'
my_age: int = 18
my_height: float = 190.1
my_gender: bool = True


# 类对象类型注解
class Student:
    pass


stu: Student = Student()

# 基础容器
# my_list: list = [1, 2, 3]
# my_tuple: tuple = (1, 2, 3)
# my_dict: dict = {"name": '彭于晏'}
# --------------------------数据容器详细注解-------------------------------
my_list: list[int] = [1, 2, 3]
my_tuple: tuple[int, int, int] = (1, 2, 3)
my_dict: dict[str, str] = {"name": '彭于晏'}

var_random = random.randint(1, 10)      # type: int
var_json = json.loads('{"name": "彭于晏"}')    # type: dict[str, str]


def fun():
    return 10


var_fun_return = fun()  # type: int

