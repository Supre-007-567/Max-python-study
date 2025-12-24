"""
全程使用面向对象思想
实现步骤
1. 设计一个类来完成数据的封装
2.设计一个抽象类，定义文件读取的相关功能，并使用子类实现具体功能
3.读取文件产生数据对象
4.进行数据需求的逻辑计算（计算每一天的销售额）
5.通过pyecharts进行图形绘制
"""
from file_define import FileReader, TextFileReader, JsonFileReader
from data_define import Record
from pyecharts.charts import Bar
from pyecharts.options import *
from pyecharts.globals import ThemeType

text_file_reader = TextFileReader('2011年1月销售数据.txt')
json_file_reader = JsonFileReader('2011年2月销售数据JSON.txt')

jan_data: list[Record] = text_file_reader.read_data()
feb_data: list[Record] = json_file_reader.read_data()

# 将两个月的数据合并
all_data: list[Record] = jan_data + feb_data

# 通过字典做数据的存储
data_dict = {}
for item in all_data:
    if item.date in data_dict.keys():
        # 当前日期已有记录
        data_dict[item.date] += item.money
    else:
        # 这是当前日期的第一条
        data_dict[item.date] = item.money


# 可视化开发
bar = Bar(init_opts=InitOpts(theme=ThemeType.LIGHT))
bar.add_xaxis(list(data_dict.keys()))
bar.add_yaxis('销售额', list(data_dict.values()), label_opts=LabelOpts(is_show=False))
bar.set_global_opts(
    title_opts=TitleOpts(title="每日销售额")
)

bar.render('每日销售额柱状图.html')



