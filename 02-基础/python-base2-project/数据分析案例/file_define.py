"""
文件相关的类定义
"""
import json

from data_define import Record

# 先定义一个抽象类用来做顶层设计，确定有哪些功能需要子类来完成
class FileReader:

    def read_data(self)->list[Record]:
        """
        读取文件数据，将读到的数据转换成 Record 对象
        将他们都封装到 list 内返回
        """
        pass


# 处理 字符串 文件
class TextFileReader(FileReader):

    def __init__(self, file_path):
        self.file_path = file_path  # 接收文件路径

    def read_data(self) -> list[Record]:
        f = open(self.file_path, 'r', encoding="UTF-8")
        # print(f.readlines())
        record_list: list[Record] = []
        for line in f.readlines():   # 拿到每一行
            line = line.strip()  # 去除左右空格和回车换行符
            data_list = line.split(',')  # 按逗号分割
            record = Record(data_list[0], data_list[1], int(data_list[2]), data_list[3])
            record_list.append(record)
            # print('record', type(record))

        f.close()
        # print(record_list)
        return record_list


# 处理 json 文件
class JsonFileReader(FileReader):

    def __init__(self, file_path):
        self.file_path = file_path

    def read_data(self) -> list[Record]:
        f = open(self.file_path, 'r', encoding="UTF-8")
        record_list: list[Record] = []
        for line in f.readlines():
            line = line.strip()
            line_dict = json.loads(line)
            record = Record(line_dict["date"], line_dict["order_id"], int(line_dict["money"]), line_dict["province"])
            print(record)
            # record_list.append(record)
        f.close()
        # print(record_list)
        return record_list


if __name__ == '__main__':
    text = TextFileReader('2011年1月销售数据.txt')
    list1 = text.read_data()
    json_test = JsonFileReader('2011年2月销售数据JSON.txt')
    list2 = json_test.read_data()
    for item in list1:
        print(item)
    for item in list2:
        print(item)

