from functools import lru_cache
from math import sqrt
#using lru cache decorator

@lru_cache(maxsize=64)
def fib(n):
    if n<2:
        return n
    else:
        return fib(n-1)+fib(n-2)
# print(fib(1000))


def dpfib(n):
    cache={0:1,1:1,2:1}
    def wrapfunc(n):
        if n in cache:
            return cache[n]
        else:
            cache[n]=wrapfunc(n-1)+wrapfunc(n-2)
            return cache[n]
    return wrapfunc(n)
# mem=dpfib(1000)
# print(mem)

def fib2(n):
    res=int(((1+sqrt(5))**n)-((1-sqrt(5)))**n)//(2**n*sqrt(5)) 
    return res
# print(fib(100))

# print(dpfib(3))

print(fib2(100))