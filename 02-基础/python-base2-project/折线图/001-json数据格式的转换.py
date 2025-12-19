"""
json 本质上是一个带有特定格式的字符串
    主要功能
     json就是一个在各个编程语言中流通的数据格式，负责不同编程语言的数据传递和交互
"""
import json

# 准备一个python列表，里面元素都是字典，将其转换为json格式

my_list = [
    {"username": '彭于晏', "age": 18},
    {"username": '邱淑贞', "age": 19},
    {"username": '胡歌', "age": 17},
    {"username": '周星驰', "age": 22},
]
json_str1 = json.dumps(my_list, ensure_ascii=False)
print(type(json_str1), json_str1)

json_str2 = '[{"username": "彭于晏", "age": 18}, {"username": "邱淑贞", "age": 19}, {"username": "胡歌", "age": 17}, {"username": "周星驰", "age": 22}]'
py_var = json.loads(json_str2)
print(type(py_var), py_var)


