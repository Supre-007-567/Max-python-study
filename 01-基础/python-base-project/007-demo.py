name = "彭于晏制造有限公司"

stock_price = 20

stock_code = "0102"

stock_price_daily_growth_factor = 1.2

growth_days = 7



print(f"公司：{name}，股票代码：{stock_code}，当前股价：{stock_price: .2f}元\n")
for i in range(growth_days):
    stock_price *= stock_price_daily_growth_factor
print(f"每日增长系数：{stock_price_daily_growth_factor}，经过{growth_days}天后，股价为：{stock_price: .2f}元")
