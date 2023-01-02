def selectionsort(arr):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]>arr[j]:
                arr[j],arr[i]=arr[i],arr[j]
                
    return arr
a=[12,2,3,4,5,6,7,9]
print(selectionsort(a))

def selectionsort2(arr):
    for i in range(len(arr)):
        min_idx=i
        for j in range(i+1,len(arr)):
            if arr[min_idx]>arr[j]:
                min_idx=j
        arr[i],arr[min_idx]=arr[min_idx],arr[i]
    return arr
a=[12,2,3,4,5,6,7,9]
print(selectionsort2(a))