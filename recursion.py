from functools import lru_cache
# fibonacchi_cache = {}


# def fibonacchi(n):
#     if n in fibonacchi_cache:
#         return fibonacchi_cache[n]
#
#     if n == 1:
#         value = 1
#     elif n == 2:
#         value = 1
#     elif n > 2:
#         value = fibonacchi(n - 1) + fibonacchi(n - 2)
#
#     fibonacchi_cache[n]=value
#     return value

#decorator for memoization
@lru_cache(maxsize=1000)
def fibonacchi(n):
    if n==1:
        return 1
    elif n==2:
        return 1
    elif n>2:
        return fibonacchi(n-1)+fibonacchi(n-2)

for n in range(1, 1000):
    print(n, ":", fibonacchi(n))
