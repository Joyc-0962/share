# 基礎多進程==========
# import multiprocessing as mp


# def job(a, d):
#     print('aaaaa')


# if __name__ == '__main__':
#     p1 = mp.Process(target=job, args=(1, 2))
#     p1.start()
#     p1.join()

# QUEUE=========
# import multiprocessing as mp
# import time
# import random


# def job(q, num):
#     res = num
#     for i in range(3):
#         res += i+i**2+i**3
#     tt = random.randint(1, 10)
#     time.sleep(tt)
#     print(num, tt)
#     q.put(res)  # queue


# if __name__ == '__main__':
#     q = mp.Queue()
#     p1 = mp.Process(target=job, args=(q, 2))
#     p2 = mp.Process(target=job, args=(q, 3))
#     p1.start()
#     p2.start()
#     p1.join()
#     p2.join()
#     res1 = q.get()
#     res2 = q.get()
#     print(res1)
#     print(res2)

# 進程鎖==========
# import multiprocessing as mp
# import time


# def job(v, num, l):
#     l.acquire()  # 锁住
#     for _ in range(5):
#         time.sleep(0.1)
#         v.value += num  # 获取共享内存
#         print(v.value)
#     l.release()  # 释放


# def multicore():
#     l = mp.Lock()  # 定义一个进程锁
#     v = mp.Value('i', 0)  # 定义共享内存
#     p1 = mp.Process(target=job, args=(v, 1, l))  # 需要将lock传入
#     p2 = mp.Process(target=job, args=(v, 3, l))
#     p1.start()
#     p2.start()
#     p1.join()
#     p2.join()


# if __name__ == '__main__':
#     multicore()

# 沒有進程鎖==========

# import multiprocessing as mp
# import time


# def job(v, num):
#     for _ in range(5):
#         time.sleep(0.1)
#         v.value += num  # 获取共享内存
#         print(v.value)


# def multicore():
#     v = mp.Value('i', 0)  # 定义共享内存
#     p1 = mp.Process(target=job, args=(v, 1))  # 需要将lock传入
#     p2 = mp.Process(target=job, args=(v, 3))
#     p1.start()
#     p2.start()
#     p1.join()
#     p2.join()


# if __name__ == '__main__':
#     multicore()


# 比較==========
import multiprocessing as mp
import time
import threading as td


def job(q):
    res = 0
    for i in range(1000000):
        res += i + i**2 + i**3
    q.put(res)  # queue


def multicore():
    q = mp.Queue()
    p1 = mp.Process(target=job, args=(q,))
    p2 = mp.Process(target=job, args=(q,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    res1 = q.get()
    res2 = q.get()
    print('multicore:', res1 + res2)


def multithread():
    q = mp.Queue()  # thread可放入process同样的queue中
    t1 = td.Thread(target=job, args=(q,))
    t2 = td.Thread(target=job, args=(q,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    res1 = q.get()
    res2 = q.get()
    print('multithread:', res1 + res2)


def normal():
    res = 0
    for _ in range(2):
        for i in range(1000000):
            res += i + i**2 + i**3
    print('normal:', res)


if __name__ == '__main__':
    st = time.time()
    normal()
    st1 = time.time()
    print('normal time:', st1 - st)
    multithread()
    st2 = time.time()
    print('multithread time:', st2 - st1)
    multicore()
    print('multicore time:', time.time() - st2)
