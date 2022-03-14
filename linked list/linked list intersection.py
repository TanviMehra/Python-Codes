def getIntersectionNode(headA,headB):
    p1=headA
    p2=headB
    while p1!=p2:
        p1=headB if p1 is None else p1.next
        p2=headA if p2 is None else p2.next
    return p1