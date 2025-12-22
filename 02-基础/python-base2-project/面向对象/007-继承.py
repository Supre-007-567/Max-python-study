"""
继承
"""


class Phone2010:
    SN = None
    producer = None
    function = None

    def __init__(self, sn, producer, function):
        self.SN = sn
        self.producer = producer
        self.function = function

    def call_by_4g(self):
        return "4G通话"


class Phone2022(Phone2010):

    def call_by_5g(self):
        return '5G通话'


# 2010手机
Iphone_X = Phone2010('007','Apple', ['4G通话', 'HiFi'])
print(f"通话：{Iphone_X.call_by_4g()}")
# 2022手机
Iphone_13 = Phone2022('567','Apple', ['4G通话', 'HiFi','faceId'])
print(f"4G通话：{Iphone_13.call_by_4g()}，5G通话：{Iphone_13.call_by_5g()}")
