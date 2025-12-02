"""
for循环
for循环是一种“轮询”机制，是对一批数据进行“逐一处理”
"""
if 0:
    userInfo = [
        {'id': '001', 'username': '彭于晏'},
        {'id': '001', 'username': '彭于晏'}
    ]

    for item in userInfo:
        print(f"用户id: {item['id']}\t用户名: {item['username']}")

    myArr = [1, 2, 3, 4]

    print(myArr)

# my_name = '彭于晏007'
# for item in my_name:
#     print(item)
#
# print(f"my_name.length={len(my_name)}")


i = 1
for i in range(9):
    # print(i)
    for j in range(i+1):
        print(f"{j+1}*{i+1}={(i+1)*(j+1)}\t", end='')
    print()



