

stu_age_list = [21, 25, 21, 23, 22, 20]

stu_age_list.append(31)

print(stu_age_list)

stu_age_list.extend([29, 33, 30])

print(stu_age_list)

print('31元素的下标',stu_age_list.index(31))


del_first = stu_age_list.pop(0)
print('删除并取出第一个元素', del_first)
length = len(stu_age_list)
del_last = stu_age_list.pop(length-1)
print("删除并取出最后一个元素", del_last)

print(f"列表最终为:{stu_age_list}")




