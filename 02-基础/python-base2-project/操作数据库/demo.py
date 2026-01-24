"""
sql 案例 读取文件 写入到 mysql 中
"""
from data_define import Record
from file_define import TextFileReader, JsonFileReader
from pymysql import Connection


jan_file_reader = TextFileReader('2011年1月销售数据.txt')
feb_file_reader = JsonFileReader('2011年2月销售数据JSON.txt')

jan_data: list[Record] = jan_file_reader.read_data()
feb_data: list[Record] = feb_file_reader.read_data()

all_data: list[Record] = jan_data + feb_data
# 构建 MySQL 链接对象
conn = Connection(
    host="localhost",
    port=3306,
    user='root',
    password='root01',
    autocommit=True
)

# 获得游标对象
cursor = conn.cursor()

# 选择数据库
conn.select_db('py_sql')

# 组织 sql
for item in all_data:
    sql = f"insert into orders(order_date,order_id,money,province) values('{item.date}', '{item.order_id}',{item.money},'{item.province}')"
    # 执行 sql
    cursor.execute(sql)
    # print(sql)
# 关闭链接
conn.close()



