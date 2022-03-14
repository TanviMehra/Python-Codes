class Queue:
    def __init__(self,capacity):
        self.queue=[None]*capacity
        print (self.queue)
        self.head=0
        self.tail=0
        self.capacity=capacity
        self.size=0

    def enqueue(self,value):
        if self.isFull():
            print('queue is full')
            return False
        self.queue[self.tail]=value
        self.tail+=1
        self.size+=1
        print (self.queue)
        return True

    def dequeue(self):
        if self.isEmpty():
            return False
        self.head+=1
        if self.head==self.tail:
            self.head=0
            self.tail=0
        self.size-=1
        print (self.queue)
        return True



    def isFull(self):
        if self.size==self.capacity:
            return True
        return False

    def isEmpty(self):
        if self.size==0:
            return True
        return False

    def getFront(self):
        if self.size==0:
            return -1
        return self.queue[self.head]

    def getRear(self):
        if self.size==0:
            return -1
        return self.queue[self.tail-1]

q=Queue(5)
print (q.enqueue(1))
print (q.enqueue(2))
print (q.enqueue(3))
print(q.enqueue(4))
print (q.enqueue(5))
print(q.enqueue(6))
print(q.dequeue())
print(q.getFront())
print(q.getRear())
print(q.dequeue())
print(q.getFront())
print(q.getRear())
print (q.dequeue())
print(q.getFront())
print(q.getRear())