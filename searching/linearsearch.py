def linearsearch(arr,key):
    for i in range(len(arr)):
        if key==arr[i]:
            return i,arr[i]
    return False
a=['god','zeus','ares','kratos','loki','thor','odin','atreus']
key='loki'
print(linearsearch(a,key))
print(a.index('loki'))