
def expandAroundCentre(s,left,right):
    count=0
    while (left>=0 and right<len(s) and s[left]==s[right]):
        count+=1
        left=left-1
        right= right+1
    return count


def countPalindrome(s):
    if len(s)==1:
        return s
    ans=0
    for i in range(len(s)):
        ans+=expandAroundCentre(s,i,i)
        ans+=expandAroundCentre(s,i,i+1)
    return ans
print (countPalindrome('aaa'))

