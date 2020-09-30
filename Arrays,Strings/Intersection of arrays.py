def set_intersection(set1,set2):
    return [x for x in set1 if x in set2]
def intersection(nums1,nums2):
    set1=set(nums1)
    set2=set(nums2)
    if len(set1)<len(set2):
        return set_intersection(set1,set2)
    else:
        return set_intersection(set2,set1)

nums1=[1,2,2,1]
nums2=[2,2]

print (intersection(nums1,nums2))

