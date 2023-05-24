import json

from pyecharts.charts import Map
from pyecharts.options import TitleOpts, VisualMapOpts

f =open("疫情.txt","r",encoding="UTF-8")
data = f.read()
f.close()

data_dict = json.loads(data)

henan_data = data_dict["areaTree"][0]["children"][3]["children"]
print(henan_data)

data_list = []
for henan in henan_data:
    city_name = henan["name"] +"市"
    city_confirm = henan["total"]["confirm"]
    data_list.append((city_name,city_confirm))

data_list.append(("济源市",55))
print(data_list)

map = Map()

map.add("河南省疫情确诊",data_list,"河南")

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

map.render("河南省疫情地图.html")


