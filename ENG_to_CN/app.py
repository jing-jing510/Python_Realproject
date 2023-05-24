# auth ： xiaokou
# date ： 2023/5/24 11:16
# pip install requests 安装
import requests

# 翻译地址
# url = "https://fanyi.baidu.com/sug"
url = "https://fanyi.baidu.com/sug"
print("欢迎使用中英文单词翻译,按q退出")
while True:
    text = input("输入中文或者英文:").strip()
    if text == "q":
        break
    data = {"kw": text}

    resp = requests.post(url, data)
    # print(data,resp)
    found = False
    if resp.status_code == 200:
        data = resp.json()
        # print(data)
        if data["errno"] == 0:
            ds = data["data"]
            for kv in ds:
                if kv['k'] == text:
                    found = True
                    print(kv['v'])
            if not found:
                print("没有找到")
        else:
            print(data)
    else:
        print(resp.content)
