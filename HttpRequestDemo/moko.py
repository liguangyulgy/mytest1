import re
import os
import urllib3


baseUrl = "http://www.moko.cc/mtb/model/%d/space.html"
imgPat = re.compile(r'http://img\S*?\.(?:jpg|jpeg|png)')
namePat = re.compile(r'<div class="username".*?<a>(.*)</a>')
shoePat = re.compile(r'<li><span>鞋码</span><b>/</b><input type="text" name="modelBean.shoes" value="([0-9]+)" />')
basePath = 'D:\scanResp'
typeDict = {"image/jpeg":".jpg","image/png":".png"}


http = urllib3.PoolManager()
for seq in range(10222,300000):
    tryUrl = baseUrl % seq
    response = http.request('GET',tryUrl)
    content = response.data.decode('UTF-8')
    name = namePat.findall(content)
    shoe = shoePat.findall(content)
    if name and int(shoe[0]) < 40:
        try:
            os.mkdir(os.path.join(basePath,name[0]))
        except:
            pass
        imgSet = {i for i in imgPat.findall(content)}
        count = 0
        for imgUrl in imgSet:
            img = http.request('GET',imgUrl)
            fileName = os.path.join(basePath,name[0],name[0]+str(count) + typeDict[img.headers['Content-Type']])
            print('seq:%d count: %d fileName %s url:%s' %(seq,count,fileName,imgUrl))
            with open(fileName,'wb') as f:
                f.write(img.data)
            count +=1

        pass
    else:
        print('jump ',seq)
        pass
