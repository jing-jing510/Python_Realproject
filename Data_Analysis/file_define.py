# auth ： xiaokou
# date ： 2023/5/26 11:11
import json
from typing import List

from data_define import Record


# 定义一个抽象类
class FileReader:
    def read_data(self) -> list[Record]:
        # 将每一条数据转到record
        pass


class TextFileReader(FileReader):

    def __init__(self, path: str):
        self.path = path

    def read_data(self) -> list[Record]:
        f = open(self.path, "r", encoding="UTF-8")
        record_list: list[Record] = []
        for line in f.readlines():
            line = line.strip()
            data_list = line.split(",")
            # 2011-01-01,b6882f5f-fb10-4210-9e45-288dd2239594,1363,广东省
            record = Record(data_list[0], data_list[1], int(data_list[2]), data_list[3])
            record_list.append(record)
        f.close()
        return record_list


class JsonFileRecorder(FileReader):
    def __init__(self, path):
        self.path = path

    def read_data(self) -> list[Record]:
        f = open(self.path, "r", encoding="UTF-8")
        record_list: list[Record] = []
        for line in f.readlines():
            data_dict = json.loads(line)
            record = Record(data_dict["date"], data_dict["order_id"], data_dict["money"], data_dict["province"])
            record_list.append(record)

        f.close()
        return record_list


if __name__ == '__main__':
    text_file_reader = TextFileReader("2011年1月销售数据.txt")
    list1 = text_file_reader.read_data()
    json_file_reader = JsonFileRecorder("2011年2月销售数据JSON.txt")
    list2 = json_file_reader.read_data()
    # text_file_reader.read_data("2011年1月销售数据.txt")
    for l in list1:
        print(l)
    for l in list2:
        print(l)
