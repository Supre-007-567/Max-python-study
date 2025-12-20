import json
from pyecharts.charts import Line
from pyecharts.options import TitleOpts, LabelOpts
# 数据处理
f_us = open("C:/Users/ASUS/Desktop/曲高和寡/02-基础/美国.txt", 'r', encoding="UTF-8")
us_data = f_us.read()
f_jp = open("C:/Users/ASUS/Desktop/曲高和寡/02-基础/日本.txt", 'r', encoding="UTF-8")
jp_data = f_jp.read()
f_in = open("C:/Users/ASUS/Desktop/曲高和寡/02-基础/印度.txt", 'r', encoding="UTF-8")
in_data = f_in.read()

# print(us_data)
# 处理开头
us_data = us_data.replace("jsonp_1629344292311_69436(", "")
jp_data = jp_data.replace("jsonp_1629350871167_29498(", "")
in_data = in_data.replace("jsonp_1629350745930_63180(", "")
# 处理结尾
us_data = us_data[:-2]
jp_data = jp_data[:-2]
in_data = in_data[:-2]
# 转换为 python 数据
us_dict = json.loads(us_data)
jp_dict = json.loads(jp_data)
in_dict = json.loads(in_data)

# print(type(us_dict), us_dict)


us_trend_data = us_dict["data"][0]['trend']
jp_trend_data = jp_dict["data"][0]['trend']
in_trend_data = in_dict["data"][0]['trend']
# print(us_trend_data)

# 获取日期列表 用于渲染 x 轴
us_x_data = us_trend_data['updateDate'][:314]
jp_x_data = jp_trend_data['updateDate'][:314]
in_x_data = in_trend_data['updateDate'][:314]

# 获取确诊 用于渲染 y 轴
us_y_data = us_trend_data['list'][0]["data"][:314]
jp_y_data = jp_trend_data['list'][0]["data"][:314]
in_y_data = in_trend_data['list'][0]["data"][:314]
# 创建折线图
line = Line()  # 构建折线图对象
# 添加 x 轴
line.add_xaxis(us_x_data)
# 添加 y 轴
line.add_yaxis("美国确诊人数", us_y_data, label_opts=LabelOpts(is_show=False))  # 添加美国的确诊人数
line.add_yaxis("日本确诊人数", jp_y_data, label_opts=LabelOpts(is_show=False))  # 添加日本的确诊人数
line.add_yaxis("印度确诊人数", in_y_data, label_opts=LabelOpts(is_show=False))  # 添加印度的确诊人数
# 全局选项
line.set_global_opts(
    title_opts=TitleOpts(title="2020年美、日、印三国确诊人数", pos_bottom="1%", pos_left="center")
)
# render 生成图表
line.render()
# 关闭文件
f_in.close()
f_us.close()
f_jp.close()



