def reverse(nums,start,end):
    while start<end:
        nums[start],nums[end]=nums[end],nums[start]
        start=start+1
        end=end-1
def rotateArray(nums,k):
    n=len(nums)
    k=k%n
    print (k)
    reverse(nums,0,n-1)
    reverse(nums,0,k-1)
    reverse(nums,k,n-1)
    return nums



nums=[1,2,3,4,5,6,7]
k=3
print (rotateArray(nums,k))
