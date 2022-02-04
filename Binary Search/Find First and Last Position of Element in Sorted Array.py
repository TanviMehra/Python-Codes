def binarySearch(nums, target, isleft):
    left= 0
    right= len(nums)-1
    while left<=right:
        mid= (left+right)//2
        # case1: checking for leftmost elements
        if nums[mid]== target:
            if isleft:
                if mid==left or nums[mid-1]!=nums[mid]:
                    return mid
                else:
                    right = mid - 1
            else:
                if mid== right or nums[mid+1]!= target:
                   return mid
                else:
                    left = mid + 1
        elif nums[mid]>target:
            right=mid-1
        else:
            left=mid+1
    return -1





def searchRange(nums, target):
    if not nums:
        return [-1,-1]
    left_index= binarySearch(nums, target,True)
    if left_index==-1:
        return [-1,-1]
    right_index= binarySearch(nums, target, False)

    return [left_index, right_index]


print (searchRange([7,8,9,10,11,12,12],12))