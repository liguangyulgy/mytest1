import urllib3
from xml.etree import ElementTree as et

http = urllib3.PoolManager()
r = http.request('GET', 'http://httpbin.org/robots.txt')
print(r.status, r.data)

r = http.request('GET','http://www.ustc.edu.cn')
print(r.status,r.data)
s = r.data.decode('utf-8')
print(r.headers)
print(r.headers['Content-Type'])
# print(s)

rr = http.request('GET','https://api.github.com/user')
print(rr)