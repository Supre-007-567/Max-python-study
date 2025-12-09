my_str = "itheima itcast boxuegu"

print(f"my_str有{my_str.count('it')}个it")

new_str = my_str.replace(" ", "|")
print(f"|替换空格{new_str}")

new_str = my_str.replace(" ", "|").split("|")
print(f"按照|分割{new_str}")







