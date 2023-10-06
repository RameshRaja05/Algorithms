#standard function

#dynamic programming:memorization
def memorize(n):
    cache={}
    def innermemorize(n):
        if (n in cache):
            return cache[n]
        else:
            print('long time')
            cache[n]=n+80
            return cache[n]
    return innermemorize
@memorize
def addto80(n):
    return n+80

print(addto80(5))
print(addto80(5))
