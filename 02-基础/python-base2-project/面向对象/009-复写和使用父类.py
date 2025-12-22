"""
复写
"""


class Phone:
    producer = 'Apple'

    def handle_call_5g(self):
        print("5G通话")


class MyPhone(Phone):
    producer = 'OPPO'

    def handle_call_5g(self):
        print("开启省电模式")
        super().handle_call_5g()
        print("通话结束，开启性能模式")


my_phone1 = Phone()
print(my_phone1.producer)
my_phone1.handle_call_5g()
print('---------------------')
# 复写
my_phone = MyPhone()
print(my_phone.producer)
my_phone.handle_call_5g()


