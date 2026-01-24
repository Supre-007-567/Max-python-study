
class Record:

    def __init__(self,create_date,order_id,money,province):
        self.create_date = create_date
        self.money = money
        self.province = province
        self.order_id = order_id

    def __str__(self):
        return f"日期：{self.create_date}，订单ID：{self.order_id}，金额：{self.money}，省份：{self.province}"


