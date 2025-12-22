"""
多继承
"""


class Phone2010:
    SN = None
    producer = 'OPPO'

    def call_by_4g(self):
        print("4G通话")


class Phone2022(Phone2010):
    def call_by_5g(self):
        print("5G通话")


class NFCReader:
    nfc_type = '5代'
    producer = 'Apple'

    def read_card(self):
        print("读卡")

    def write_card(self):
        print("写卡")


class RemoteControl:
    rc_type = '红外遥控'

    def control(self):
        print("开启红外遥控")


class MyPhone(Phone2022, NFCReader, RemoteControl):
    pass


my_phone = MyPhone()
my_phone.call_by_5g()
my_phone.control()
my_phone.read_card()
my_phone.write_card()
print(my_phone.producer)
