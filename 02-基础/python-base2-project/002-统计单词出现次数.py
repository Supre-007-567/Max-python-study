"""
通过⽂件读取操作，读取此⽂件，统计itheima单词出现的次数
"""
times1 = 0
times2 = 0
with open("C:/Users/ASUS/Desktop/曲高和寡/02-基础/file-python-txt2.txt","r",encoding="UTF-8") as f:
    for line in f:
        if line.count("itheima"):
            times2 += line.count("itheima")
    times1 = f.read().count("itheima")

print(f"方法①：\nitheima出现了{times1}次")
print(f"方法②：\nitheima出现了{times2}次")
