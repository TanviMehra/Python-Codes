class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList:

    def __init__(self):
        self.head = None

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
        list_size = self.listLength()
        if index > list_size:
            return -1
        current = self.head
        current_idx = 0
        while (current):
            if current_idx == index:
                return current.val
            current_idx += 1
            current = current.next

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        current = Node(val)
        current.next = self.head
        self.head = current

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        newNode = Node(val)
        if self.head:
            current = self.head
            while (current.next):
                current = current.next
            current.next = newNode
        else:
            self.head = newNode

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index > self.listLength():
            return
        cur_idx = 0
        current = self.head
        newNode = Node(val)
        if index == 0:
            newNode.next = self.head
            self.head = newNode
        else:
            while True:
                if cur_idx == index - 1:
                    newNode.next=current.next
                    current.next=newNode
                    '''previous = current
                    nextnode = current.next
                    previous.next = newNode
                    newNode.next = nextnode'''
                    return
                cur_idx += 1
                current = current.next

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index >= self.listLength():
            return None
        current_idx = 0
        current = self.head
        if current_idx == index:
            self.head = current.next
        else:
            while (current):
                if current_idx == index - 1:
                    current.next=current.next.next
                    '''previous = current
                    nextnode = current.next.next
                    previous.next = nextnode'''
                current_idx += 1
                current = current.next


    def printLList(self):
        current=self.head
        my_list=[]
        while(current):
            my_list.append(current.val)
            current=current.next
        return my_list

# Your MyLinkedList object will be instantiated and called as such:
obj = MyLinkedList()
["MyLinkedList","addAtHead","addAtHead","addAtHead","addAtIndex","deleteAtIndex","addAtHead","addAtTail","get","addAtHead","addAtIndex","addAtHead"]
[[],[7],[2],[1],[3,0],[2],[6],[4],[4],[4],[5,0],[6]]
# param_1 = obj.get(index)
obj.addAtHead(7)
obj.addAtHead(2)
obj.addAtHead(1)
print (obj.printLList())
obj.addAtIndex(3,0)
print (obj.printLList())
obj.deleteAtIndex(2)
print (obj.printLList())
obj.addAtHead(6)
print ('here',obj.printLList())
obj.addAtTail(4)
print (obj.printLList())
print (obj.get(4))
print (obj.printLList())
obj.addAtHead(4)
print (obj.printLList())
obj.addAtIndex(5,0)
obj.addAtHead(6)
print(obj.printLList())
