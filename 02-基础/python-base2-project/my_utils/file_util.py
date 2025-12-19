"""
print_file_info(file_name) 接收传入的文件路径，打印文件的全部内容，如果文件不存在，输出提示信息，接收文件路径，通过 finally 关闭文件对象
append_to_file(file_name,data) 接收文件路径以及传入数据，将数据追加写入到文件中
"""


def print_file_info(file_name):
    try:
        f = open(file_name, 'r', encoding="UTF-8")
        print(f.read())
    except Exception as e:
        print(e)
        f = open(file_name, 'w', encoding="UTF-8")
        f.write("曲高和寡")
        f.write("\n抽刀断水水更流")
    finally:
        print("文件关闭")
        f.close()


def append_to_file(file_name, data):
    print("append is being executing")
    f = open(file_name, 'a', encoding="UTF-8")
    f.write(data)
    f.close()
    print("append has benn completely executed")


