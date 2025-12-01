"""
99乘法表
"""
i = 1
j = 1
while i <= 9:
    # print(f"i={i}")
    while j <= i:
        print(f"{j} x {i} = {i * j}\t", end='')
        j += 1
    i += 1
    j = 1
    print()

