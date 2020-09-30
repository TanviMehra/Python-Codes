from collections import defaultdict

def arrayIntersection(nums1,nums2):
    numDict=defaultdict(int)
    output=[]
    for val in nums1:
        numDict[val]+=1
    for val in nums2:
        if val in numDict and numDict[val]>=1:
            output.append(val)
            numDict[val]-=1
    return output


nums1=list(map(int,input().split()))
nums2=list(map(int,input().split()))
if len(nums1)>len(nums2):
    print (arrayIntersection(nums1, nums2))
else:
    print (arrayIntersection(nums2, nums1))

#print(arrayIntersection(nums1,nums2))











nums1=[4,9,5]
nums2=[9,4,9,8,4]

'''intersect = []
for val in nums1:
    if val in nums2:
        intersect.append(val)
        nums2.remove(val)

return (intersect)'''