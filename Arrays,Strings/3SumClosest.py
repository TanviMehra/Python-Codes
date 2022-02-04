def threeSumClosest(nums, target):
    closest = float('inf')
    nums.sort()
    for i in range(len(nums)):
         closest=twoSum(nums, i, closest, target)
    return closest


def twoSum(nums, i, closest, target):
    low = i + 1
    high = len(nums) - 1
    while low < high:
        sum_val = nums[i] + nums[high] + nums[low]
        if  abs(target - sum_val)<abs(closest):
            closest = sum_val
        if sum_val < target:
            low = low + 1
        elif sum_val > target:
            high = high - 1
        else:
            print('here')
            closest = target
            break
    return closest

nums=[-1,2,1,-4]
target=1
print (threeSumClosest(nums,target))
