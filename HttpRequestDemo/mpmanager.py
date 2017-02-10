import multiprocessing,os,time

def workTask(d,l):
    d[1] = '1'
    d['2'] = 2
    d[0.25] = None
    l.reverse()

def managerDemo():
    with multiprocessing.Manager() as manager:
        d = manager.dict()
        l = manager.list(range(10))

        p = multiprocessing.Process(target=workTask, args=(d,l))
        p.start()
        p.join()

        print(d)
        print(l)

def f(x):
    return x*x

def queueJoin(q):
    q.put('heew')

def demoQueue():
    q = multiprocessing.Queue()
    p = multiprocessing.Process(name='hello',target=queueJoin,args=(q,))
    p.start()
    p.join()
    print('hello')


def testY(n):
    i = 1
    while i <= n:
        yield i
        i+=1

def poolDemo():
    with multiprocessing.Pool(4) as pool:
        print(pool.map(f,testY(10)))

        for i in pool.imap_unordered(f,range(10)):
            print(i)

        # evaluate "f(20)" asynchronously
        res = pool.apply_async(f,(20,))
        print(res.get(timeout=1))

        res = pool.apply_async(os.getpid,callback=f)
        print(res.get(timeout=1))

        multiple_results = [pool.apply_async(os.getpid) for i in range(4)]
        print([res.get(timeout=1) for res in multiple_results])

        res = pool.apply_async(time.sleep,(10,))

        try:
            print(res.get(timeout=1))
        except multiprocessing.context.TimeoutError:
            print('We lacked patience and got a multiprocessing.TimeoutError')

        print('For the moment, the pool remains available for more work')

    print('Now the pool is closed')

def pipeJoin(b):
    b.send('teshl')

def pipeDemo():
    (a,b) = multiprocessing.Pipe()
    pp = multiprocessing.Process(target=pipeJoin,args=(b,))
    pp.start()
    print(a.recv())
    pp.join()

if __name__ == '__main__':
    pipeDemo()