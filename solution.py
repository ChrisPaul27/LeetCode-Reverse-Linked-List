# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        dummy = None
        prev = dummy
        succ = dummy
        curr = head
        if head != None:
            succ = head.next
        
        while curr and succ and succ.next:
            nextPoint = succ.next
            curr.next = prev
            succ.next = curr
            
            prev = succ
            curr = nextPoint
            succ = nextPoint.next
        if curr != None:
            curr.next = prev
        if succ != None:
            succ.next = curr
            return succ
        return curr
        
