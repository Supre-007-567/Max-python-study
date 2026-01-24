my_list: [int] = []
for index in range(3):
    num = float(input(f"请输入第{index+1}个数"))
    my_list.append(num)
my_sum = sum(my_list)
print(f"和{my_sum: .3f}")










