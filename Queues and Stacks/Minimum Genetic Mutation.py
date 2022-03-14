from collections import deque
class Solution():
    def openLock(self,start,end,bank):
        bank=set(bank)
        print (bank)
        seen=set()
        seen.add(start)
        queue=deque([start])
        level=0
        while queue:
            size= len(queue)
            print (level)
            print (queue)
            print (len(queue))
            for _ in range(size):
                node= queue.popleft()
                if node==end:
                    return level
                else:
                    for i in range(len(node)):
                        for char in ['A', 'C', 'G', 'T']:
                            mutated = node[:i] + char + node[i + 1:]
                            if mutated not in seen and mutated in bank:
                                seen.add(mutated)
                                queue.append(mutated)
            level+=1
        return -1




start= "AACCGGTT"
end=  "AAACGGTA"
bank= ["AACCGGTA", "AACCGCTA", "AAACGGTA"]
obj=Solution()
print (obj.openLock(start,end,bank))
