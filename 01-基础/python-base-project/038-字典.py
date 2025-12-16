employee_data = [
    {"姓名": "王力鸿", "部门": "科技部", "工资": 3000, "级别": 1},
    {"姓名": "周杰伦", "部门": "市场部", "工资": 5000, "级别": 2},
    {"姓名": "林俊杰", "部门": "市场部", "工资": 7000, "级别": 3},
    {"姓名": "张学油", "部门": "科技部", "工资": 4000, "级别": 1},
    {"姓名": "刘德滑", "部门": "市场部", "工资": 6000, "级别": 2}
]
#
print("操作之前")
for item in employee_data:
    print(item)
print("操作之后")
for item in employee_data:
    if item["级别"] == 1:
        item["级别"] += 1
        item["工资"] += 1000
for item in employee_data:
    print(item)
