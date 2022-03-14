class Node:
    def __init__(self,val):
        self.val=val
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def insert(self,data):
        newNode=Node(data)
        if self.head:
            current=self.head
            while(current.next):
                current=current.next
            current.next=newNode
        else:
            self.head=newNode


    def addAtIndex(self,index,val):
        cur_idx=0
        current=self.head
        newNode = Node(val)
        if index==0:
            newNode.next=self.head
            self.head=newNode
        else:
            while True:
                if cur_idx==index-1:
                    previous=current
                    nextnode=current.next
                    previous.next=newNode
                    newNode.next=nextnode
                    return
                cur_idx+=1
                current=current.next


    def listLength(self):
        current=self.head
        count=0
        while(current):
            count=count+1
            current=current.next
        return count

    def printLList(self):
        current=self.head
        while(current):
            print(current.val)
            current=current.next
    # iterative approach using 3 pointers
    def reverseList(self):
        previous =None
        current=self.head
        next=None
        while(current):
            next=current.next
            current.next=previous
            previous=current
            current=next
        return previous

    def printLListRev(self,prev):
        current = prev
        while (current):
            print(current.val)
            current = current.next



obj=LinkedList()
obj.insert(23)
obj.insert(6)
obj.insert(15)
obj.printLList()
prev= (obj.reverseList())
obj.printLListRev(prev)
#print (obj.listLength())
#print (obj.get(5))
#obj.delete(15)
#obj.printLList()
#obj.deleteAtIndex(2)
