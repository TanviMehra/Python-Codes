#important point - do it in place without using extra space
# the array is sorted so all similar elements appear together

def removeDuplicates(nums):
    i=0
    j=0
    while i<len(nums)and j<len(nums):
        if nums[i]==nums[j]:
            j=j+1
        else:
            i=i+1
            nums[i]=nums[j]
            j=j+1
    return i+1


nums=list(map(int,input().split()))
print (removeDuplicates(nums))


'''slow_pointer=0
        for current_pointer in range(1,len(nums)):
            if (nums[slow_pointer]!=nums[current_pointer]):
                slow_pointer+=1
                nums[slow_pointer]=nums[current_pointer]
        return (slow_pointer+1)
'''