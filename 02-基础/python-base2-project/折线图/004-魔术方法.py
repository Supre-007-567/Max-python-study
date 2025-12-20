"""

"""


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Student对象：name={self.name}，age={self.age}"

    def __lt__(self, other):
        return self.age < other.age


stu1 = Student('彭于晏', 18)
stu2 = Student('胡歌', 20)
print(f"stu1<stu2 ? -> {stu1 < stu2}")





