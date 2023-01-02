basket=[12,45,90,7,1,4,6,88,13]
def bubblesort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
print(bubblesort(basket))#o(n^2)


def bubblesort2(arr):
    for i in range(len(arr),-1):
        for j in range(len(arr)-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
print(bubblesort2(basket))#o(n^2)