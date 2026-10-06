# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: Optional[ListNode]
        :type val: int
        :rtype: Optional[ListNode]
        """
        dummy=ListNode(0)
        dummy.next=head
        tail=dummy
        while tail and tail.next:
            if tail.next.val==val:
                tail.next=tail.next.next
            else:
                tail=tail.next
        return dummy.next
