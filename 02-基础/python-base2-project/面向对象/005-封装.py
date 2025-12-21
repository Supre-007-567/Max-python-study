"""
私有属性
"""


class IPhone:
    __IEMI = None
    producer = None
    __sn = 'abbcd3289482'

    def __get_system_info(self):
        print("系统信息")

    def get_name(self):
        print("IPhone13")

    def call_sb(self):
        if self.__IEMI > 0:
            print(self.__IEMI)
            print(f"此机器sn码为:{self.__sn}")
            print("正在拨打")
            import winsound
            for i in range(5):
                winsound.Beep(500, 500)
        else:
            print("权限不足")

    def __init__(self, iemi,producer):
        self.__IEMI = iemi
        self.producer = producer


iphone1 = IPhone(8, 'Apple')
iphone1.call_sb()

