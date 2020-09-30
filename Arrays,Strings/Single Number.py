#Given a non-empty array of integers, every element appears twice except for one. Find that single one.

from collections import Counter
def singleNumber(nums):
    numsDict=Counter(nums)
    print (numsDict)
    for key,value in numsDict.items():
        if value==1:
            return key

def singleNumberXor(nums):
    single_number=0
    for val in nums:
        single_number^=val
    return single_number

nums= [4,1,2,1,2]
print (singleNumber(nums))
#Xor operation finds the single number in place without using extra space based on the logic
# that xor of two same numbers is 0 and XOR of single number with zero is the single number
print (singleNumberXor(nums))

