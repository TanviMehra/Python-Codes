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

    def listLength(self):
        current=self.head
        count=0
        while(current):
            count=count+1
            current=current.next
        return count

    def printLList(self):
        my_list=[]
        current=self.head
        while(current):
            my_list.append(current.val)
            current=current.next
        return my_list
    # iterative approach using 3 pointers

    def removeElements(self, val):
        previous= Node(0)
        previous.next=self.head
        current=self.head
        while(current):
            if current.val==val:
                previous.next=current.next
            else:
                previous=current
            current=current.next
        return previous.next

    def printLListdeleted(self,previous):
        my_list=[]
        current=previous
        while(current):
            my_list.append(current.val)
            current=current.next
        return my_list



obj=LinkedList()
obj.insert(1)
#obj.insert(1)
#obj.insert(1)
obj.insert(2)
obj.insert(6)
obj.insert(3)
obj.insert(4)
obj.insert(5)
obj.insert(6)
#print (obj.printLList())
previous=obj.removeElements(6)
#print (obj.listLength())
#print (obj.get(5))
#obj.delete(15)
print (obj.printLListdeleted(previous))
#obj.deleteAtIndex(2)
