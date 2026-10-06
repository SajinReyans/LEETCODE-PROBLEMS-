# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        slow=head
        fast=head
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
        temp=slow
        prev=None
        while temp:
            nxt=temp.next
            temp.next=prev
            prev=temp
            temp=nxt
        
        check1=head
        check2=prev
        while check1 and check2:
            if check1.val!=check2.val:
                return False
            check1=check1.next
            check2=check2.next
        return True
        
