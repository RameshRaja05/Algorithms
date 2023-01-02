s='hello'
#using iteration
def rev(n):
    li=[]
    for i in range(len(s)-1,-1,-1):
        li.append(n[i])
    return ''.join(li)
print(rev(s))
#using recursion
def rever2(n):
    if n=='':
        return ''
    else:
        return rever2(n[1:])+n[0]
print(rever2(s))
#using closure 
def rever3(n):
    arr=list(n[0:])
    revarr=[]
    def addtoarr(a):
        if(len(a)>0):
            revarr.append(a.pop())
            addtoarr(a)
    addtoarr(arr)
    return ''.join(revarr)
print(rever3(s))