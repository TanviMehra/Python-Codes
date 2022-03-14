from collections import deque
class Solution():
    def neighbors(self,node):
        neigh_list=[]
        for i in range(4):
            current_position=int(node[i])
            s1= node[:i]+str(0 if current_position==9 else current_position+1)+node[i+1:]
            s2= node[:i]+str(9 if current_position==0 else current_position-1)+node[i+1:]
            neigh_list.append(s1)
            neigh_list.append(s2)
        return neigh_list
    def openLock(self,deadends,target):
        dead=set(deadends)
        seen=set()
        seen.add('0000')
        queue=deque(['0000'])
        level=0
        while queue:
            size= len(queue)
            print (level)
            print (queue)
            print (len(queue))
            for _ in range(size):
                node= queue.popleft()
                if node==target:
                    return level
                if node in dead:
                    continue
                else:
                    for nei in self.neighbors(node):
                        if nei not in seen:
                            seen.add(nei)
                            queue.append(nei)
            level+=1
        return -1








deadends=["0201","0101","0102","1212","2002"]
target= "0202"
obj=Solution()
print (obj.openLock(deadends,target))
