"""
类的成员方法
"""
if 0:
    # 初始对象
    # 设计一个类
    class Student:
        name = None
        gender = None
        nationality = None
        native_place = None
        age = None
    # 创建一个对象
    stu1 = Student()
    # 对象属性进行赋值
    stu1.name = "彭于晏"
    stu1.age = 18
    stu1.gender = '男'
    stu1.nationality = 'China'
    stu1.native_place = '河南郑州'
    # 获取对象中记录的信息 （输出）
    print(stu1.name)
"""
成员方法
"""


class Student:
    name = None

    def sayHi(self, greeting="多多关照"):
        print(f"你好，我是{self.name}。{greeting}")


stu1 = Student()
stu1.name = '胡歌'
stu1.sayHi()

stu2 = Student()
stu2.name = "邱淑贞"
stu2.sayHi("初来乍到，多多关照")






