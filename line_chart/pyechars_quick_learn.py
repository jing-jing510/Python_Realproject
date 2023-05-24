# auth ： xiaokou
# date ： 2023/5/24 17:06
# import pyecharts

from pyecharts.charts import Line
from pyecharts.options import *
from pyecharts.types import Legend

line = Line()

line.add_xaxis(["中国", "美国", "英国"])

line.add_yaxis("GDP", [30, 50, 10])

line.set_global_opts(
    title_opts= TitleOpts(title="GDP展示", pos_left="centert", pos_bottom="1%"),
    legend_opts= LegendOpts(is_show=True),
    toolbox_opts= ToolboxOpts(is_show=True),
    visualmap_opts= VisualMapOpts(is_show=True)
)

line.render()
