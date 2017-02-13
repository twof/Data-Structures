from multiprocessing import Pool
import random

arr = random.sample(range(100), 10)

def h(item):
    return item*item


if __name__ == '__main__':
    with Pool(5) as p:
        print(p.map(h, arr))
