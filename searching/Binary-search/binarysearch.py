from time import time
a=[1,2,4,5,6,89,90]
key=90

#recursive way
time1=time()
def binarysearch(arr,key,low,high):
    if low<=high:
        mid=low+(high-low)//2
        if key==arr[mid]:
            return True
        elif key>arr[mid]:
            return binarysearch(arr,key,mid+1,high)
        elif key<arr[mid]:
            return binarysearch(arr,key,low,mid-1)
    else:
        return False
time2=time()
print(f"recursive way{time2-time1}")
print(binarysearch(a,key,0,len(a)-1))
time3=time()




def binarysearch2(arr,key):
    low=0
    high=len(arr)
    while(low<=high):
        mid=low+(high-low)//2
        if key==arr[mid]:
            return True
        elif key<arr[mid]:
            high=mid-1
        elif key>arr[mid]:
            low=mid+1
    return -1
time4=time()
print(f"Iterative way{time4-time3}")
print(binarysearch2(a,key))
