# auth ： xiaokou
# date ： 2023/5/24 11:25
import requests
# url = "https://fanyi.baidu.com/sug"
# text = input("输入中文或者英文:").strip()
# data = {"kw": text}
# resp = requests.post(url, data)
# data = resp.json()
# print(data) #{'errno': 0, 'data': [{'k': 'Apple', 'v': 'n. 苹果公司，原称苹果电脑公司'}, {'k': 'apple', 'v': 'n. 苹果; 苹果公司; 苹果树'}, {'k': 'APPLE', 'v': 'n. 苹果'}, {'k': 'apples', 'v': 'n. 苹果，苹果树( apple的名词复数 ); [美国口语]棒球; [美国英语][保龄球]坏球; '}, {'k': 'Apples', 'v': '[地名] [瑞士] 阿普勒'}]}
url ="https://fanyi.baidu.com/v2transapi"

text = input("请输入中文或英文:").strip()
langdetect = requests.post("https://fanyi.baidu.com/langdetect",text)
v2tran = requests.post("https://fanyi.baidu.com/v2transapi?from=zh&to=en",text)
print(langdetect)
print(v2tran)
print(v2tran.json())
print(langdetect.json())

