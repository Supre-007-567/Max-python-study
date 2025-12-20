"""

"""


class Student:
    stu_list = []

    def stu_add(self, name, age):
        self.stu_list.append({'name': name, 'age': age})


def add_action():
    name = input("请输入学生姓名\n")
    age = input("请输入学生年龄\n")
    stu1.stu_add(name, age)


stu1 = Student()
for i in range(3):
    print(f"当前录入第{i+1}位学生，总共需要录入3位学生信息")
    add_action()
print(stu1.stu_list)
