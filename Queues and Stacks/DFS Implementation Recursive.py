def DFSRecursive(graph,current,target,visited):
    if current==target:
        return True
    for neigh in graph[current]:
        if neigh not in visited:
            visited.add(next)
        return DFSRecursive(graph,neigh,target,visited)==True




graph= {'A':['B','C','D'],'B':['E'],'C':['E','F'],'D':['G'],'E':[],'F':[],'G':[]}
visited=set()
print (DFSRecursive(graph,'A','G',visited))