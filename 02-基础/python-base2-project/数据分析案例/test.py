"""

"""
import json
# f1 = open('2011年1月销售数据.txt','r',encoding="UTF-8")
# for item in f1:
#     print(item)
f1 = open('2011年2月销售数据JSON.txt', 'r', encoding="UTF-8")
for item in f1.readlines():
    item = item.strip()    # 去除空格和换行
    item_py = json.loads(item)  # 逐行 json -> py
    # print(type(item_py))
    print(f"日期：{item_py['date']}，订单id：{item_py['order_id']}，金额：{item_py['money']}，省份：{item_py['province']}")

