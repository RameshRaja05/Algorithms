from functools import lru_cache
@lru_cache(maxsize=32)
def addto80(n):
    return n+80
print(addto80(5))
print(addto80(5))