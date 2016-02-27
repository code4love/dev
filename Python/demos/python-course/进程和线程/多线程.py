# -*- coding: utf-8 -*-

import time, threading

# 新线程执行的代码:
def loop():
    print('thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('thread %s ended.' % threading.current_thread().name)

def testLoop():
    print('thread %s is running...' % threading.current_thread().name)
    t = threading.Thread(target=loop, name='LoopThread')
    t.start()
    t.join()  # 等待子线程运行完成
    print('thread %s ended.' % threading.current_thread().name)

balance = 0
def change_it(n):
    # 先存后取，结果应该为0:
    global balance
    balance = balance + n
    balance = balance - n

def run_thread(n):
    for i in range(500000):
        change_it(n)

lock = threading.Lock()
def run_thread_lock(n):
    for i in range(500000):
        # 先要获取锁:
        lock.acquire()
        try:
            # 放心地改吧:
            change_it(n)
        finally:
            # 改完了一定要释放锁:
            lock.release()

def test_thead_lock():
    t1 = threading.Thread(target=run_thread_lock, args=(5,))
    t2 = threading.Thread(target=run_thread_lock, args=(8,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    #不加锁最后的balance不一定为0
    print(balance)

def main():
    #testLoop()
    test_thead_lock()

if __name__ == '__main__':
    main()