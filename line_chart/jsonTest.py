# auth ： xiaokou
# date ： 2023/5/24 16:56

import json

data = [{"name": "老王", "age": 16}, {"name": "老王", "age": 16}]

data1 = json.dumps(data)
print(data1,type(data1))

data2 = json.loads(data1)
print(data2,type(data2))
