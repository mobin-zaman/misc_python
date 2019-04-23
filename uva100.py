from sys import stdin
import functools


@functools.lru_cache(None)
def cycle_number(i):
    count = 1

    while(1):
        if(i == 1):
            return count
        if(i % 2 == 0):
            i /= 2
        else:
            i = (i*3+1)
        count += 1


@functools.lru_cache(None)
def max_cycle_number(start, end):
    start, end = min(start, end), max(start, end)
    return max(cycle_number(i) for i in range(start, end+1))


if __name__ == '__main__':
    for line in stdin:
        start, end = map(int, line.split())
        print(start, end, max_cycle_number(start, end))
