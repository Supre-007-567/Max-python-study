"""
通过⽂件读取操作，读取此⽂件，统计itheima单词出现的次数
"""
times = 0
with open("C:/Users/ASUS/Desktop/曲高和寡/02-基础/file-python-txt2.txt","r",encoding="UTF-8") as f:
    for line in f:
        print(type(line))
        if line.count("itheima"):
            times += line.count("itheima")
print(f"itheima出现了{times}次")
