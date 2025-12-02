"""
break continue
"""

for item in range(1, 4):
    # if item == 2:
    #     break
    # if item == 2:
    #     continue
    print(f"1、外层循环执行{item}")
    for temp in range(1, 5):
        print(f"2、内层循环执行{temp}")
