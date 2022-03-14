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
        my_list=[]
        while(current):
            my_list.append(current.val)
            current=current.next
        return my_list

    def isPallindrome(self):
        if self.head==None:
            return True
        first_half_end= self.findEnd(self.head)
        second_half_start= self.reverseList(first_half_end.next)
        result=True
        first=self.head
        second=second_half_start
        while result and  second is not None:
            if first.val!=second.val:
                result=False
            first=first.next
            second=second.next
        first_half_end.next= self.reverseList(second_half_start)
        return result


    def findEnd(self,head):
        slow=head
        fast=head
        while fast.next is not None and fast.next.next is not None:
            fast=fast.next.next
            slow=slow.next
        return slow

    # iterative approach using 3 pointers

    def reverseList(self,head):
        previous =None
        current=head
        next=None
        while(current):
            next=current.next
            current.next=previous
            previous=current
            current=next
        return previous

    def printLListRev(self,prev):
        current = prev
        my_list=[]
        while (current):
            my_list.append(current.val)
            current = current.next
        return my_list



obj=LinkedList()
obj.insert(23)
obj.insert(6)
obj.insert(23)
print (obj.isPallindrome())
#print (obj.listLength())
#print (obj.get(5))
#obj.delete(15)
#obj.printLList()
#obj.deleteAtIndex(2)
