def rotateArray(nums,k):
    nums[:]=nums[-k:]+nums[:-k]
    return (nums)

nums= [-1,-100,3,99]
k=2
print(rotateArray(nums,k))