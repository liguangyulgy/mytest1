import requests
import json

# r = requests.get('https://api.github.com/events')
# print(r)
#print(r.text)

# pp = requests.post('http://httpbin.org/post')
# print (pp.status_code)
# print (pp.text)

payload = {'key1':'va==  lue1','key2':['valu67&^&e2','helloworld',3445]}
# r = requests.get('http://httpbin.org/get',params=payload)
# print(r.url)
# print(r.text)
# v = json.loads(r.text)
# print(v)

# r = requests.post('http://httpbin.org/post',json=payload)
# print (r)
# print(r.text)
# print(r.json())

s = requests.Session()
s.get('http://httpbin.org/cookies/set/sessioncookie/123456789')
r = s.get('http://httpbin.org/cookies')

print(r.text)

s.auth=('user','pass')
s.headers.update({'x-test':'false'})
r1 = s.get('http://httpbin.org/headers')
r2 = s.get('http://httpbin.org/headers',headers={'x-test':'true'})

print(r1.json())
print(r2.text)






