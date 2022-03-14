# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        list1 = ''
        list2 = ''
        while l1:
            list1 += str(l1.val)
            l1 = l1.next
        while l2:
            list2 += str(l2.val)
            l2 = l2.next

        if len(list1) > len(list2):
            for i in range(len(list1) - len(list2)):
                list2 += str(0)
        elif len(list2) > len(list1):
            for i in range(len(list2) - len(list1)):
                list1 += str(0)
        list1 = list1[::-1]
        list2 = list2[::-1]
        list3 = [val for val in str(int(list1) + int(list2))][::-1]

        fakehead = ListNode(-1)
        prev = fakehead
        for val in list3:
            prev.next = ListNode(int(val))
            prev = prev.next
        return fakehead.next





