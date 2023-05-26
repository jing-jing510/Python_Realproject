# auth ： xiaokou
# date ： 2023/5/26 15:23
from pyecharts.options import TitleOpts, LabelOpts

from file_define import FileReader,JsonFileRecorder,TextFileReader
from data_define import Record
from pyecharts.charts import Bar

text_file_reader = TextFileReader("2011年1月销售数据.txt")
jan_data = text_file_reader.read_data()
json_file_reader = JsonFileRecorder("2011年2月销售数据JSON.txt")
feb_data = json_file_reader.read_data()

all_data = jan_data + feb_data

# 相同天 数据计算
data_dict = {}
for record in  all_data:
    if record.date in data_dict.keys():
        data_dict[record.date] += record.money
    else:
        data_dict[record.date] = record.money
print(data_dict)

# 可视化
bar = Bar()

bar.add_xaxis(list(data_dict.keys()))
bar.add_yaxis("销售额",list(data_dict.values()),label_opts=LabelOpts(is_show=False))
bar.set_global_opts(
    title_opts=TitleOpts(title="每日销售额")
)

bar.render("每日销售额柱状图.html")