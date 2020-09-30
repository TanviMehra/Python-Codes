
def intersect(nums1,nums2):
    nums1=sorted(nums1)
    nums2=sorted(nums2)
    i,j,k=0,0,0
    while i<len(nums1) and j<len(nums2):
        if nums1[i]<nums2[j]:
            i=i+1
        elif nums1[i]>nums2[j]:
            j=j+1
        else:
            nums1[k]=nums1[i]
            k+=1
            i+=1
            j+=1
    return nums1[:k]


nums1=[]
nums2=[]
print (intersect(nums1,nums2))









nums1=[1,2,2,1]
nums2=[2,2]