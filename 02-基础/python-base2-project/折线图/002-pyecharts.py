"""
pyecharts 折线图
"""
from pyecharts.charts import Line

# 得到折线图对象
line = Line()
# 添加 x 轴数据
line.add_xaxis(['Japan', 'America', 'Chain'])
# 添加 x 轴数据
line.add_yaxis("GDP", [20, 80, 40])
# 生成图标
line.render()

