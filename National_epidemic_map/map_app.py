"""

    演示地图可视化的基本使用
"""
from pyecharts.charts import Map
from pyecharts.options import *

map = Map()

# 准备数据
data = [
    ("北京市", 99),
    ("上海市", 199),
    ("天津市", 929),
    ("湖南省", 399),
    ("浙江省", 499),
    ("河北省", 599),
    ("河南省", 699)
]

map.add("名称:测试地图", data, "china")

map.set_global_opts(
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[
            {"min": 1, "max": 9, "label": "1-9", "color": "#ccffff"},
            {"min": 10, "max": 99, "label": "1-9", "color": "#FF4445"},
            {"min": 100, "max": 999, "label": "1-9", "color": "#990033"}
        ]
    )
)

map.render()
