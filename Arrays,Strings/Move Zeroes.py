def moveZeroes(arr):
    i=0
    for j in range(len(arr)):
        if arr[j]!=0:
            arr[i]=arr[j]
            i=i+1
            print (i)
    return (arr[:i]+[0]*(len(arr)-i))
arr=[0,1,0,3,12,0,78,9,0,8,4,5,0,0]
print (moveZeroes(arr))