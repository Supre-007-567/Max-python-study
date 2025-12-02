"""
for 循环
"""
if 0:
    times = 0
    my_str = 'itheima is a brand of itcast'
    for item in my_str:
        if item == 'a':
            times += 1
    print(f"a出现了{times}次")

"""
for 循环语句，本质上遍历的是：序列类型
    range(num)
    获取一个从 0 开始，到 num 结束的数字序列(不含num本身)
    如 range(5) 取得的数据是:[0,1,2,3,4]
"""
if 0:
    for item in range(5):
        print(item)
if 1:
    count = 0
    my_num = 100
    for item in range(my_num):
        if item % 2 == 0:
            count += 1
        print(item)
    print(f"0-{my_num-1}(不含100本身)有{count}个偶数")

