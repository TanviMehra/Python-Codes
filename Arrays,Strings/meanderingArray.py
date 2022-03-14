import heapq
def meanderingArray(unsorted):
    unsorted.sort(reverse=True)
    #sort_array= sorted(unsorted, reverse=True)
    start=0
    end=len(unsorted)-1
    out=[]
    while start<=end:
        if start==end:
            out.append(unsorted[start])

        else:
            out.append(unsorted[start])
            out.append(unsorted[end])
        start=start+1
        end=end-1
    return out


# Using two heaps - min heap and max heap
def meandering(unsorted):
    heap1,heap2= [],[]
    for val in unsorted:
        heapq.heappush(heap1,-val)
        heapq.heappush(heap2,val)
    out=[]
    while len(out)!=len(unsorted):
        out.append(-heapq.heappop(heap1))
        if len(out)!= len(unsorted):
            out.append(heapq.heappop(heap2))
    return out

print (meanderingArray([5,2,7,8,-2,25,25]))
print (meandering([5,2,7,8,-2,25,25]))