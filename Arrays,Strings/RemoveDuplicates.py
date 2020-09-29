#Using the two pointer approach to remove duplicates in place-
# fast pointer traverses the array while
# slow pointer points to first element.

def removeDuplicates(nums):
    if len(nums)==0:
        return 0
    else:
        slow=0
        for fast in range(1,len(nums)):
            if (nums[slow]!=nums[fast]):
                slow=slow+1
                nums[slow]=nums[fast]
        print (nums[:slow+1])
nums=list(map(int,input().split()))
removeDuplicates(nums)