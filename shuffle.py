import random

def shuffle(nums:[]) -> []:
    for i in range(len(nums)-1, 0, -1):
        j = random.randint(0, i-1)
        tmp = nums[i]
        nums[i] = nums[j]
        nums[j] = tmp
    return nums

nums = [1,2,3,4,5]
s = shuffle(nums)
print(s)
