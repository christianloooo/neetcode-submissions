# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = head
        tr = head
        leng = 0
        while dummy:
            dummy = dummy.next
            leng += 1
        i = leng - n
        if leng <= 1:
            return None
        elif leng == n:
            return head.next
        for s in range(i-1):
            tr = tr.next
        tr.next = tr.next.next
        return head