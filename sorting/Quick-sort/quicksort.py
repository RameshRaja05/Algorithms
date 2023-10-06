from time import time
time1=time()
def quicksort(arr,low,high):
    if low<high:
        partitionindex=partition(arr,low,high)
        
        quicksort(arr,low,partitionindex-1)
        quicksort(arr,partitionindex+1,high)

count=0
def partition(arr,left,right):
    smallerin=left-1
    pivot=arr[right]
    for i in range(left,right):
        if arr[i]<pivot:
            global count
            count+=1
            smallerin+=1
            arr[smallerin],arr[i]=arr[i],arr[smallerin]
    arr[smallerin+1],arr[right]=arr[right],arr[smallerin+1]
    # print(arr)
    # print(count)
    return smallerin+1
time2=time()
print(f"lemuto implementation{time2-time1}")
a=[99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
quicksort(a,0,len(a)-1)
print(a)



time3=time()
def quicksort2(arr,low,high):
    if low<high:
        partitionpos=partition2(arr,low,high)
        quicksort2(arr,low,partitionpos)
        quicksort2(arr,partitionpos+1,high)
def partition2(arr,low,high):
    pivot=arr[low]
    i=low
    j=high
    while(True):
        while(arr[i]<pivot):
            i+=1
        while(arr[j]>pivot):
            j-=1
        if(i>=j):
            return j
        arr[i],arr[j]=arr[j],arr[i]
time4=time()
print(f"hoare's implementation{time4-time3}")
b=[99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
quicksort2(b,0,len(b)-1)
print(b)
