# https://juejin.im/post/5bf4a862518825396d71f402#heading-8
# https://zhuanlan.zhihu.com/p/44656243
def merge(left, right):
    result = []

    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    while left:
        result.append(left.pop(0))
    while right:
        result.append(right.pop(0))

    return result
def mergesort(arr):
    if len(arr) < 2:
        #print("arr:", arr)
        return arr
    mid = len(arr) // 2
    #print("arr:", arr)
    #print("mid:", mid)

    return merge(mergesort(arr[0:mid]), mergesort(arr[mid:]))

arr = [3,7,5,1,6,2,4] 
print(mergesort(arr))
