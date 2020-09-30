#yo check if dulpicates exists in an array
def containsDuplicate(nums):
    numsDict={}
    for num in nums:
        if num in numsDict:
            return True
        else:
            numsDict[num]=1
    return False
nums=list(map(int,input().split()))
print (containsDuplicate(nums))