"""
文件写入
"""
# 打开一个文件(这个文件并不存在，mode = w 会自动创建)
import time

f = open("C:/Users/ASUS/Desktop/曲高和寡/02-基础/file-python-txt3.txt", "w", encoding="UTF-8")
# write 写入
# f.write("Hello,the file operation of Python4")
# f.flush()  # 将内存中积攒的内容写入到硬盘中
# time.sleep(3)
#
# f.close()  # 关闭文件，close 函数自带 flush 功能
f.write("test2\n")
f.write("test3\n")
f.write("test4\n")
f.close()
