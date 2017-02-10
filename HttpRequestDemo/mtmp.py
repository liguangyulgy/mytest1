# Similarity and difference of multi thread vs. multi process
# Written by Vamei

import os
import threading
import multiprocessing
import queue
import time

# worker function
def worker(sign, lock,qq):
    # lock.acquire()
    print(sign, os.getpid())
    print(__name__)
    time.sleep(1)
    return 'Hello'
    # lock.release()



# # Multi-thread
# record = []
# lock  = threading.Lock()
# for i in range(5):
#     thread = threading.Thread(target=worker,args=('thread',lock))
#     thread.start()
#     record.append(thread)
#
# for thread in record:
#     thread.join()

# Multi-process
def test():
    record = []
    lock = multiprocessing.Lock()
    qq = multiprocessing.Queue()
    for i in range(5):
        process = multiprocessing.Process(target=worker,args=('process',lock,qq))
        process.start()
        record.append(process)

    for process in record:
        process.join()

def test2():
    pool = multiprocessing.Pool(5)
    for i in range(5):
        pool.apply_async(func=worker,args=('process2',None,None),callback=callback)
    pool.close()
    pool.join()

def callback(arg):
    print('callback',arg)



if __name__ == '__main__':
    print('hello world')
    # Main
    print('Main:', os.getpid())
  #  test()
    test2()