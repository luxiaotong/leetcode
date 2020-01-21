#https://blog.csdn.net/zhusongziye/article/details/79113918
def quicksort(arr, start, end):
    if start >= end:
        return arr

    left, right = start, end
    pivot = arr[left]

    while start < end:
        print("pivot, start, end:", pivot, start, end)
        print("arr0:", arr)
        while start < end and arr[end] >= pivot:
            end -= 1
        while start < end and arr[start] <= pivot:
            start += 1
        arr[start], arr[end] = arr[end], arr[start]
        print("arr1:", arr)

    arr[start], arr[left] = arr[left], arr[start]
    #arr[end], arr[left] = arr[left], arr[end]
    print("left, start, end:", left, start, end)
    print("arr2:", arr)
    quicksort(arr, left, start-1)
    quicksort(arr, end+1, right)

    return arr

#print(quicksort([5,6,4,2], 0, 3))

arr = [2,3,5,7,1,4,6,15,5,2,7,9,10,15,9,17,12]
print(quicksort(arr, 0, len(arr)-1))
