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

    # get the value at the index specified by the user
    def get(self,index):
        if index>=self.listLength():
            return None
        count=0
        current=self.head
        while (current):
            if count==index:
                return current.val
            count=count+1
            current=current.next

    def delete(self,data):
        current=self.head
        if current.val==data:
            self.head=current.next
        else:
            while (current.next!=None):
                if current.next.val==data:
                    previous=current
                    nextnode=current.next.next
                    previous.next=nextnode
                current=current.next

    def deleteAtIndex(self,index):
        if index>=self.listLength():
            return None
        current_idx=0
        current=self.head
        if current_idx == index:
            self.head = current.next
        else:
            while(current):
                if current_idx==index-1:
                    previous=current
                    nextnode=current.next.next
                    previous.next=nextnode
                current_idx += 1
                current = current.next





obj=LinkedList()
obj.insert(23)
obj.insert(15)
obj.insert(6)
#obj.printLList()
#print (obj.listLength())
#print (obj.get(5))
#obj.delete(15)
#obj.printLList()
#obj.deleteAtIndex(2)
obj.addAtIndex(3,5)
obj.printLList()
["MyLinkedList","addAtHead","addAtHead","addAtHead","addAtIndex","deleteAtIndex","addAtHead","addAtTail","get","addAtHead","addAtIndex","addAtHead"]
[[],[7],[2],[1],[3,0],[2],[6],[4],[4],[4],[5,0],[6]]