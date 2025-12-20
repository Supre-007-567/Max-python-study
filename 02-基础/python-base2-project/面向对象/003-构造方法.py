"""
构造方法
"""


class Student:
    name = None
    age = None
    tel = None

    def __init__(self, name='xx', age=0, tel='123'):
        self.name = name
        self.age = age
        self.tel = tel
        print("Student类创建了一个对象")


stu1 = Student('彭于晏', 18, '17634504689')
print(stu1.name)
print(stu1.age)
print(stu1.tel)

