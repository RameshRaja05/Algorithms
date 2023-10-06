#fib numbers without using array or list
def fib(n):
    # this is unpacking in python.in js it's called destructuring
    prev, cur, su = [0, 1, 0]
    if (n < 2):
        return n
    else:
        i = 2
        while (i <= n):
            su = prev+cur
            prev = cur
            cur = su
            i += 1
    return su
#time complexity=o(n)
#space complexity=o(1)


print(fib(8)) #21

#fib numbers using array or list
def fib2(n):
    li=[0,1]
    if n<2:
        return n
    else:
        for i in range(2,n+1):
            li.append(li[i-2]+li[i-1])
    return li[n]
    #time complexity=o(n)
    #space complexity=o(n)
print(fib2(12)) #144

#fib numbers using beginner complicated recursion
calc=0
def fib3(n):
    global calc
    calc+=1
    if n<2:
        return n
    else:
        return fib3(n-1)+fib(n-2)
    #time complexity=o(2^n)
    #space complexity=o(1)
print(fib3(50),calc) #233