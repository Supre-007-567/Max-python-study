"""
连接数据库
"""
from pymysql import Connection
# 构建到 MySQL 数据库的链接
conn = Connection(
    host="localhost",  # 主机名
    port=3306,  # 默认 3306
    user='root',
    password='root01',
    autocommit=True
)

# 执行非查询性 SQL
cursor = conn.cursor()  # 获取到游标
conn.select_db("heima_python1")
# 插入性 sql
cursor.execute("insert into test_pymysql values(5,'林青霞')")
# commit 确认修改
# conn.commit()
# 关闭连接
conn.close()
