# def mergesort(arr):
#     if(len(arr)==1):
#         return arr
#     low=0
#     high=len(arr)
#     mid=low+(high-low)//2
#     left,right=arr[:mid],arr[mid:]
   
#     return merge(mergesort(left),mergesort(right))
# def merge(left,right):
#     res=[]
#     i=j=0
#     while(i<len(left) and j<len(right)):
#         if(left[i]<right[j]):
#             res.append(left[i])
#             i+=1
#             # print(f"left:{res}")
#         else:
#             res.append(right[j])
#             j+=1
#             # print(f"right:{res}")
#     return res+left[i:]+right[j:]
# # a=[239,12,34,45,90,4,200,58]
# # mergesort(a)

def mergesort2(arr):
    if len(arr)==1:
        return arr
   
    mid=len(arr)//2
    left,right=arr[:mid],arr[mid:]
    mergesort2(left)
    mergesort2(right)
     

    i=j=k=0
    while(i<len(left) and j<len(right)):
        if(left[i]<=right[j]):
            arr[k]=left[i]
            i+=1
        else:
            arr[k]=right[j]
            j+=1
        k+=1
    while(i<len(left)):
        arr[k]=left[i]
        i+=1
        k+=1
    while(j<len(right)):
        arr[k]=right[j]
        j+=1
        k+=1
   
a=[239,12,34,45,90,4,200,58]
print(mergesort2(a))
print(a)#o(nlogn)