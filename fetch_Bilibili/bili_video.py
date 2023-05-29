# auth ： xiaokou
# date ： 2023/5/29 15:38
#
"""
    爬虫思路
        数据来源分析
            通过开发者工具进行抓包分析,分析视频来源

            源代码 ctrl+F 搜索 playinfo 可以找到响应的数据内容
        代码实现
            发送请求,模拟浏览器对于视频详情页url地址发送请求
            获取数据,获取服务器返回响应数据
            解析数据,提取我们想要数据类型 视频标题以及视频基本信息
            保存数据,保存本地
"""
import json
import re
import subprocess
from pprint import pprint

# 第三方模块 pip install requests
import requests

# 确定请求url地址
url = 'https://www.bilibili.com/video/BV1wr4y1j7fh'
# 发送请求,模拟浏览器对于视频详情页url地址发送请求
#  请求头 headers  伪装代码
#     伪装是为了防止被识别是爬虫程序
headers = {
    'referer': 'https://www.bilibili.com/video',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.57'
}
# 发送数据
response = requests.get(url=url, headers=headers)
# 获取数据
# response.text
# print(response.text)
# 解析数据
"""
    正则表达式 -->提取解析
    
"""
title = re.findall('"title":"(.*?)","pubdate"', response.text)[0]
playinfo = re.findall('<script>window.__playinfo__=(.*?)</script>', response.text)[0]
print('-----------------')
print(title)
print(playinfo)
# pprint(playinfo)
print(('----------------'))
data_dict = json.loads(playinfo)
pprint(data_dict)
audio_data = data_dict['data']['dash']['audio'][0]['baseUrl']
video_data = data_dict['data']['dash']['video'][0]['baseUrl']
print(video_data)
print(audio_data)
print('------------')
audio_content = requests.get(url=audio_data, headers=headers).content
video_content = requests.get(url=video_data, headers=headers).content

with open('video\\' + title + '.mp3', mode="wb") as audio:
    audio.write(audio_content)
with open('video\\' + title + '.mp4', mode="wb") as video:
    video.write(video_content)
# 合成
# cmd = u"ffmpeg -i video\\{title}.mp4 -i video\\{title}.mp3 -c:v copy -c:a copy video\\{title}output.mp4"
# subprocess.run(cmd, shell=True)
