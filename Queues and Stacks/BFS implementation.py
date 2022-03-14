from collections import deque

def findTargetLength(graph,startnode,target):
    queue=deque(startnode)
    dist=0
    visited=set()
    visited.add(startnode)
    while queue:
        dist+=1
        size=len(queue)
        for i in range(size):
            node=queue.popleft()
            if node==target:
                return dist
            else:
                if node in graph:
                    for n in graph[node]:
                        if n not in visited:
                            queue.append(n)
                            visited.add(n)
    return -1

graph= {'A':['B','C','D'],'B':['E'],'C':['E','F'],'D':['G']}
print (findTargetLength(graph,'A','G'))



