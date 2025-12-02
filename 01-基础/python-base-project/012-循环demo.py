"""
99乘法表
"""
i = 1
while i <= 9:
    # print(f"i={i}")
    j = 1
    while j <= i:
        print(f"{j} x {i} = {i * j}\t", end='')
        j += 1
    i += 1
    print()

