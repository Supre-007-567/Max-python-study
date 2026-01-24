import json

from data_define import Record

class FileReader:

    def Reader(self):
        pass

class TextReader(FileReader):

    def __init__(self, path):
        self.path = path

    def Reader(self) -> list[Record]:
        f = open(self.path,'r',encoding="UTF-8")
        record_list: list[Record] = []
        for line in f.readlines():
            line = line.strip()
            record = line.split(",")
            record = Record(create_date=record[0],order_id=record[1],money=record[2],province=record[3])
            record_list.append(record)
        return record_list


class JsonReader(FileReader):

    def __init__(self,path):
        self.path = path

    def Reader(self) -> list[Record]:
        f = open(self.path,'r',encoding="UTF-8")
        record_list: list[Record] = []
        for line in f.readlines():
            line = line.strip()
            line = json.loads(line)
            # print(line)
            record = Record(create_date=line["date"],order_id=line["order_id"],money=line["money"],province=line["province"])
            record_list.append(record)
        return record_list


if __name__ == '__main__':
    text_obj = TextReader('2011年1月销售数据.txt')
    text_list = text_obj.Reader()
    for item in text_list:
        print(item)
    json_obj = JsonReader("2011年2月销售数据JSON.txt")
    json_list = json_obj.Reader()
    for item in json_list:
        print(item)



