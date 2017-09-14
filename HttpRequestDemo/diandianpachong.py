import re
import urllib3
import os

pat = re.compile(r'http://\S*?\.jpg')
nexturl1 = "http://www.moko.cc/mtb/model/2942666/space.html"
nexturl = "http://www.moko.cc/mtb/model/%d/space.html"

try:
    path = os.path.join(os.path.dirname(__file__),'test1')
    os.mkdir(path)
    os.chdir(path)
except IOError:
    pass
except SyntaxError as s:
    print(s)

http = urllib3.PoolManager()
count = 10000

while count < 30000:
    print('Page', count)
    myurl = nexturl % count
    myres = http.request('GET', myurl)
    uc = myres.data.decode('utf-8')

    mat = pat.findall(uc)

    if len(mat) > 2:

        urlSet = {i for i in mat}

        cnt = 1
        for item in urlSet:
            print('Page %s, No. %s, url: %s' % (count,cnt,item))
            cnt += 1
            fnp = re.compile('(\w{10}\.\w+)$')
            fnr = fnp.findall(item)
            if fnr:
                fname = fnr[0]
                img = http.request('GET',item)
                with open(os.path.join(path,fname),'wb') as f :
                    f.write(img.data)
    else:
        print('noData')

    count +=1