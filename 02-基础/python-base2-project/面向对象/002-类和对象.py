"""
类和对象
"""
# 涉及一个闹钟类


class Clock:
    id = None
    price = None

    def ring(self):
        import winsound
        winsound.Beep(500, 3000)

# 构建 2 个闹钟对象并让其工作


clock1 = Clock()
clock1.id = '007'
clock1.price = '19,99'
print(f"闹钟信息：id：{clock1.id}，价格{clock1.price}")
clock1.ring()
