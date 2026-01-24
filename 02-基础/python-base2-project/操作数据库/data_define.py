"""
数据定义的类
"""


class Record:

    def __str__(self):
        return f"Record类对象：日期{self.date}，订单id：{self.order_id}，金额{self.money}，省份：{self.province}"

    def __init__(self, date, order_id, money, province):
        self.date = date
        self.order_id = order_id
        self.money = money
        self.province = province



