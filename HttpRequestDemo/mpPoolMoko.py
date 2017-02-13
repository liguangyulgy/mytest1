import multiprocessing,re,os,urllib3
import threading
import requests

baseUrl = "http://www.moko.cc/mtb/model/%d/space.html"
imgPat = re.compile(r'http://img\S*?\.(?:jpg|jpeg|png)')
namePat = re.compile(r'<div class="username".*?<a>(.*)</a>')
shoePat = re.compile(r'<li><span>鞋码</span><b>/</b><input type="text" name="modelBean.shoes" value="([0-9]+)" />')
basePath = 'D:\scanResp'
typeDict = {"image/jpeg":".jpg","image/png":".png"}

http = urllib3.PoolManager(20)



def findGirls(start,step,qq):
    for seq in range(start,30000000,step):
        url = baseUrl % seq
        rsp = http.request('GET',url)
        content = rsp.data.decode('utf-8')
        name = namePat.findall(content)
        shoe = shoePat.findall(content)
        if name and int(shoe[0]) < 40:
            qq.put((name[0],content))
            print(threading.current_thread().getName(), 'find', name)
        else:
            print(threading.current_thread().getName(), 'jump', seq)
            pass

def dlPic(fname,url):
    img = http.request('GET',url)
    fname  += typeDict[img.headers['Content-Type']]
    print('download %s from %s' % (fname,url))
    with open(fname,'wb') as f:
        f.write(img.data)

def getPicUrl(qq):
    while True:
        name,content = qq.get(block = True)
        urls = imgPat.findall(content)
        cont = 0
        dirname = os.path.join(basePath,name)
        try:
            os.mkdir(dirname)
        except IOError:
            pass
        for url in set(urls):
            fname = os.path.join(dirname, name + str(cont))
            threading.Thread(target=dlPic,args=(fname,url)).start()
            cont+=1

def main():
    for i in range(1,10):
        pool.apply_async(func=findGirls,args=(10200+i,10,queue))
    for i in range(1,10):
        pool.apply_async(func=getPicUrl,args=(queue,))

if __name__ == '__main__':
    with multiprocessing.Pool(20) as pool:
        manager = multiprocessing.Manager()
        queue = manager.Queue()
        main()
        pool.close()
        pool.join()
