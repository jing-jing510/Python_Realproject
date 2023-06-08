import urllib3
import urllib.request
resp = urllib3.request("GET", "http://www.baidu.com")
# urllib.request.urlopen()
urllib3.request()
print(dir(urllib))
print(dir(urllib3))
# print(resp.status)
print(resp.data)
