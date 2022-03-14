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
        current=self.head
        while(current):
            print(current.val)
            current=current.next

    def oddEvenList(self):
        odd_list_pointer=Node(0)
        even_list_pointer=Node(0)
        odd_head= odd_list_pointer
        even_head=even_list_pointer
        counter=1
        while self.head:
            if counter%2!=0:
                odd_list_pointer.next=self.head
                odd_list_pointer=odd_list_pointer.next
            else:
                even_list_pointer.next=self.head
                even_list_pointer=even_list_pointer.next
            self.head=self.head.next
            counter=counter+1
        even_list_pointer.next=None
        odd_list_pointer.next=even_head.next
        return odd_head.next

    def printLListNew(self,odd_head):
        my_list=[]
        current = odd_head
        while (current):
            my_list.append(current.val)
            current = current.next
        return my_list


obj=LinkedList()
obj.insert(2)
obj.insert(1)
obj.insert(3)
obj.insert(5)
obj.insert(6)
obj.insert(4)
obj.insert(7)
obj.printLList()
odd_head=obj.oddEvenList()
print (obj.printLListNew(odd_head))

#print (obj.listLength())
#print (obj.get(5))
#obj.delete(15)

#obj.deleteAtIndex(2)
