def backtrack(ans, sub, nums, i):
    if i == len(nums):
        return
    sub.append(nums[i])
    ans.append(sub)
    print("num:", nums[i:])
    print("sub:", sub)
    print("ans:", ans)
    print("i:", i)
    print()
    for j in range(i+1, len(nums)):
        backtrack(ans, sub[:], nums, j)
def subsets(nums: [int]) -> [[int]]:
    ans = []
    ans.append([])
    for i in range(len(nums)):
        backtrack(ans, [], nums, i)
    return ans
print(subsets([1,2,3]))
