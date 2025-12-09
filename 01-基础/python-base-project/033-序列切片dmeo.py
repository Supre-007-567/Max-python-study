# my_str = "万过薪月，员序程马黑来，nohtyp学"
# 得到 "黑马程序员"
# new_str = my_str[::-1]
# start = new_str.index("黑")
# end = new_str.index("员")
# result = new_str[start:end + 1:1]
# print(result)

my_str = "万过薪月，员序程马黑来，nohtyp学"
new_str = my_str[::-1]
split_str = new_str.split("，")
result = split_str[1].replace("来", "")
print(result)
















