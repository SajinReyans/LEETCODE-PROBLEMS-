# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head or not head.next:
            return head
        prev=None
        newHead=head
        while newHead:
            nxt=newHead.next
            newHead.next=prev
            prev=newHead
            newHead=nxt
        return prev
