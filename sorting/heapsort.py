def heapify(arr, n, i):
    largest = i
    left = 2*i+1
    right = 2*i+2
    if left < n and arr[largest] < arr[left]:
        largest = left
    if right < n and arr[largest] < arr[right]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heapsort(arr):
    n = len(arr)
    # covert a list into heap
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)
    # extract the elememnt
    for j in range(n-1, 0, -1):
        arr[j], arr[0] = arr[0], arr[j]
        heapify(arr, j, 0)


a = [45, 89, 76, 34, 22, 11, 90]
heapsort(a)
print(a)
