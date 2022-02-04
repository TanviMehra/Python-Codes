def checkIntersection(arr1,arr2):
    i = 0
    j = 0
    out = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] == arr2[j]:
            out.append(arr1[i])
            i = i + 1
            j = j + 1
        elif arr1[i] < arr2[j]:
            i = i + 1
        else:
            j = j + 1
    return(out)
def arraysIntersection(arr1, arr2, arr3):
    output=checkIntersection(arr1,arr2)
    res=checkIntersection(arr3,output)
    return res







arr1= [197,418,523,876,1356]
arr2 = [501,880,1593,1710,1870]
arr3 = [521,682,1337,1395,1764]
print (arraysIntersection(arr1,arr2,arr3))



