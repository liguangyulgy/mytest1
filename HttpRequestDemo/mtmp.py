# Similarity and difference of multi thread vs. multi process
# Written by Vamei

import os
import threading
import multiprocessing
import queue

# worker function
def worker(sign, lock,qq):
    # lock.acquire()
    print(sign, os.getpid())
    print(__name__)
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
        record.append(process)

    for process in record:
        process.start()
        process.join()
    print(qq)

if __name__ == '__main__':
    print('hello world')
    # Main
    print('Main:', os.getpid())
    test()