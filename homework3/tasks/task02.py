import time
import struct
import random
import hashlib

from multiprocessing import Pool


def slow_calculate(value):
    """Some weird voodoo magic calculations"""
    time.sleep(random.randint(1, 3))
    data = hashlib.md5(str(value).encode()).digest()
    return sum(struct.unpack("<" + "B" * len(data), data))


if __name__ == "__main__":
    with Pool(48) as p:
        answer = sum(p.map(slow_calculate, range(0, 500)))
