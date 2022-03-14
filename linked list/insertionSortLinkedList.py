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



    def printLList(self):
        current=self.head
        while(current):
            print(current.val)
            current=current.next

    def insertionSortList(self):
        DummyHead = Node(-1)
        if self.head:
            DummyHead.next = self.head
            fake_pointer = DummyHead
            current = self.head.next
            while current:
                if current.val < fake_pointer.next.val:
                    current.next = fake_pointer.next
                    fake_pointer.next = current
                    current=current.next

                else:
                    while current.val >fake_pointer.next.val:
                        fake_pointer = fake_pointer.next
                    current.next = fake_pointer.next
                    fake_pointer.next = current
                    fake_pointer = DummyHead
                    current = current.next
        return DummyHead.next


obj=LinkedList()
obj.insert(4)
obj.insert(2)
obj.insert(1)
obj.insert(3)

obj.printLList()
obj.insertionSortList()
obj.printLList()
