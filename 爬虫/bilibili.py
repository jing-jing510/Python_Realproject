# auth ： xiaokou
# date ： 2023/6/8 15:31

import requests

url = "https://api.bilibili.com/x/web-interface/ranking/v2?rid=0&type=all"


def get_json(url):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.41'
    }
    try:
        html = requests.get(url, headers=headers)
        return html.json()

    except BaseException:
        print('request error')
        pass


print(get_json(url=url))