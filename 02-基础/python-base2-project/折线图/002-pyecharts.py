"""
pyecharts 折线图
"""
from pyecharts.charts import Line
from pyecharts.options import TitleOpts, LegendOpts, ToolboxOpts, VisualMapOpts
# 得到折线图对象
line = Line()
# 添加 x 轴数据
line.add_xaxis(['Japan', 'America', 'Chain'])
# 添加 x 轴数据
line.add_yaxis("GDP", [20, 80, 40])


# 设置全局配置 set_global_opts 来设置
line.set_global_opts(
    # 标题
    title_opts=TitleOpts(title="GDP展示", pos_left="center", pos_bottom="1%"),
    # 图例
    legend_opts=LegendOpts(is_show=True),
    # 工具箱
    toolbox_opts=ToolboxOpts(is_show=True),
    # 视觉映射
    visualmap_opts=VisualMapOpts(is_show=True)
)

# 生成图标
line.render()
