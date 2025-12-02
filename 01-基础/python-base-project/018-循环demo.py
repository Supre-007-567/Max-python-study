"""
某公司账户余额有 1W 元，给20名员工发工资
    员工编号从 1-20 从编号1开始 一次领取工资 每人可领取1000元
    领工资时 财务判断员工绩效分 (1-10) (随机生成),如果低于5，不发工资 换下一位
    如果工资发完了，结束发工资
"""
import random
total = 10000
salary = 1000
for item in range(1, 21):
    temp = random.randint(1, 10)
    if total <= 0:
        print("工资发放完毕：余额耗尽")
        break
    elif temp < 5:
        print(f"{item}号员工绩效不足，下一位")
        continue
    else:
        total -= salary
        print(f"{item}号员工发工资，余额: {total}")

print(f"工资发放完毕，所剩余额：{total}")










