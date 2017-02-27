from fibonacci2 import Fib




def triangles():
    pass
    a=[1]
    while True:
        yield a
        b = [0] * (1+len(a))
        for index,val in enumerate(a):
            b[index] +=val
            b[index +1] += val
        a = b
n = 0
for t in triangles():
    print(t)
    n += 1
    if n == 10 :
        break


from contextlib import contextmanager

@contextmanager
def testWith(a):
    print('hello')
    yield a
    print('world')

if __name__ == '__main__':
    for n in Fib(100):
        print(n,end=',')
    with testWith('124324') as b:
        print(b)


