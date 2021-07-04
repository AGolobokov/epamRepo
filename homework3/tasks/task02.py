import multiprocessing
import time
import struct
import random
import hashlib


def slow_calculate(value):
    """Some weird voodoo magic calculations"""
    time.sleep(random.randint(1, 3))
    data = hashlib.md5(str(value).encode()).digest()
    return sum(struct.unpack('<' + 'B' * len(data), data))


def worker(procnum, return_dict):
    return_dict[procnum] = slow_calculate(procnum)


if __name__ == '__main__':
    manager = multiprocessing.Manager()
    return_dict = manager.dict()
    jobs = []

    for i in range(0,3):
        p = multiprocessing.Process(target=worker, args=(i, return_dict))
        jobs.append(p)
        p.start()

    for proc in jobs:
        proc.join()
    print(return_dict.values())
    sum = 0
    for i in return_dict.values():
        sum+= i
    print(sum)