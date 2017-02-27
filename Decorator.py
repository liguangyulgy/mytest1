


def deco(arg):
    def _deco2(func):
        def _deco(*args,**kwargs):
            print('before %s called[%s]' % (func.__name__, arg))
            func(*args,**kwargs)
            print('after %s called[%s]' % (func.__name__, arg))
        return _deco
    return _deco2

@deco('stest')
def myfunction(a,b):
    print('myfunc(%s,%s) called.' % (a,b) )

myfunction(11,22)
myfunction(44,55)

class locker:
    def __init__(self):
        print('locker.__init__() should be not called.')

    @staticmethod
    def acquire():
        print('locker.acquire() called.(staticmethod)')

    @staticmethod
    def release():
        print('locker.release() called (staticmethod)')

def clsdeco(cls):
    def _deco(func):
        def _decof(*args,**kwargs):
            print('befor %s called [%s].' % (func.__name__,cls))
            cls.acquire()
            try:
                func(*args,**kwargs)
            finally:
                cls.release()
        return _decof
    return _deco

@clsdeco(locker)
def myfunc(a,b,c,d):
    print('myfunc %s,%s,%s,%s' % (a,b,c,d))


myfunc(1,2,3,4)
