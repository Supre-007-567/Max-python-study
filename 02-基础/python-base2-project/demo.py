"""
文件备份
"""
fr = open("C:/Users/ASUS/Desktop/曲高和寡/02-基础/bill.txt", "r", encoding="UTF-8")

fw = open("C:/Users/ASUS/Desktop/曲高和寡/02-基础/bill.txt.bak", "w", encoding="UTF-8")

for line in fr:
    if line.count("测试"):
        continue
    fw.write(line)
fr.close()
fw.close()
