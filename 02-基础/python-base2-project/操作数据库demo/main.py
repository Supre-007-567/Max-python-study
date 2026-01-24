from file_define import JsonReader, TextReader

from pymysql import Connection
conn = Connection(
    host='localhost',
    port=3306,
    user='root',
    password='root01',
    autocommit=True
)

cursor = conn.cursor()
conn.select_db('py_sql')

text_obj = TextReader('2011年1月销售数据.txt')
text_list = text_obj.Reader()
json_obj = JsonReader('2011年2月销售数据JSON.txt')
json_list = json_obj.Reader()

all_data = text_list+json_list
for record in all_data:
    print(record)
    sql = f"insert into orders values('{record.create_date}','{record.order_id}',{record.money},'{record.province}')"
    cursor.execute(sql)


cursor.close()






