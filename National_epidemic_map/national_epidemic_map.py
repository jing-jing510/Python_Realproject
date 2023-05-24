import json

from pyecharts.charts import Map
from pyecharts.options import *

# 读取文件
f = open("疫情.txt", "r", encoding="UTF-8")
# f.read()
data = f.read()
print(data)
f.close()

data_dict = json.loads(data)

province_data_list = data_dict["areaTree"][0]["children"]

data_list = []
for pro in province_data_list:
    # 数据中没有添加 省 市 自治区
    province_name = pro["name"]
    if province_name == "北京" or province_name == "天津" or province_name == "上海" or province_name == "重庆":
        province_name += "市"
    elif province_name == "广西":
        province_name += "壮族自治区"
    elif province_name == "宁夏":
        province_name += "回族自治区"
    elif province_name == "新疆":
        province_name += "维吾尔自治区"
    elif province_name == "西藏" or province_name == "内蒙古":
        province_name += "自治区"
    else:
        province_name += "省"
    province_confirm = pro["total"]["confirm"]
    data_list.append((province_name, province_confirm))

print(data_list)

map = Map()

map.add("各省份确诊人数", data_list, "china")

map.set_global_opts(
    title_opts=TitleOpts(title="全国疫情地图"),
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[
            {"min": 1, "max": 99, "label": "1-99人", "color": "#E66B1A"},
            {"min": 100, "max": 999, "label": "1-999人", "color": "#7B9966"},
            {"min": 1000, "max": 4999, "label": "1-4999人", "color": "#4474BB"},
            {"min": 5000, "max": 9999, "label": "1-9999人", "color": "#AA55AA"},
            {"min": 10000, "max": 19999, "label": "1-19999人", "color": "#F73809"},
            {"min": 20000, "max": 999999, "label": "1-99999人", "color": "#C4C43C"}
        ]
    )
)
map.render("全国疫情确诊地图.html")
