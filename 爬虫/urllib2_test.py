import urllib3
resp = urllib3.request("GET", "http://httpbin.org/robots.txt")

print(resp.status)
print(resp.data)