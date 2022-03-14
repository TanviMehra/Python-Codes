class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class MyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def listLength(self):
        count = 0
        current = self.head
        while (current):
            count += 1
            current = current.next
        return count

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index >= self.size:
            return -1
        current = self.head
        for i in range(index):
            current = current.next
        return current.val

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        newNode = Node(val)
        if self.head:
            self.head.prev = newNode
            newNode.next = self.head
            # newNode.prev=None
            self.head = newNode
            self.size += 1
        else:
            self.head = newNode
            self.size += 1

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        newNode = Node(val)
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = newNode
            newNode.next = None
            newNode.prev = current
            self.size += 1
        else:
            self.head = newNode
            self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        newNode = Node(val)
        if index > self.size:
            return

        if index == 0:
            self.addAtHead(val)
        else:
            current = self.head
            for i in range(1, index):
                current = current.next
            newNode.next = current.next
            current.next = newNode
            newNode.prev = current
            # current.next.prev=newNode
            self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index >= 0 and index < self.size:
            self.size -= 1
            if index == 0:
                self.head = self.head.next
            else:
                prev = self.head
                cur = self.head.next

                i = 1
                while i < index:
                    prev = cur
                    cur = cur.next
                    i += 1

                prev.next = cur.next

    def deleteElementByValue(self,val):
        if self.head is None:
            return
        #handle if value is equal to head
        elif self.head.val==val:
            self.head=self.head.next
        current=self.head
        #handle all mid values
        while current and current.next:
            print (current.val)
            if current.val==val:
                print ('yes')
                current.prev.next=current.next
                current.next.prev=current.prev
                return
            current=current.next
        #check if value in the tail
        if current.val==val:
            current.prev.next=None

    def printLList(self):
        current=self.head
        my_list=[]
        while(current):
            my_list.append(current.val)
            current=current.next
        return my_list

obj= MyLinkedList()
obj.addAtHead(1)
obj.addAtIndex(1,2)
obj.addAtIndex(2,3)
obj.addAtIndex(3,4)
obj.addAtIndex(4,5)
obj.addAtTail(6)
print (obj.printLList())
obj.deleteElementByValue(6)
print(obj.printLList())
obj.addAtHead(7)
obj.addAtIndex(1,8)
obj.addAtIndex(4,9)
print(obj.printLList())