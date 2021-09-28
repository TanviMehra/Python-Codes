'''t= 3002
requests=[1,100,3001,3002]
ran=[t-3000,t]
count=0
for val in requests:
    if val in range(t-3000,t+1):
        count=count+1
print (count)'''


from collections import deque
class RecentCounter:
    def __init__(self):
        self.requests=deque()

    def ping(self,t):
        ran = [t - 3000, t]
        self.requests.append(t)
        while self.requests:
            if self.requests[0] < ran[0]:
                self.requests.popleft()
            else:
                break
        return (len(self.requests))

obj=RecentCounter()
param1=obj.ping(1)
print (param1)
param2=obj.ping(100)
print (param2)
param3= obj.ping(3001)
print (param3)
param4= obj.ping(3002)
print (param4)
param5=obj.ping(3003)
print (param5)
