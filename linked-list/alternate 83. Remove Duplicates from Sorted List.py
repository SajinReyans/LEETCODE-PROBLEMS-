# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        
        slow = head
        fast = head

        while fast and fast.next :
            fast=fast.next
            if fast.val == slow.val:
                slow.next = fast.next
            else:
                slow=slow.next
            # fast=fast.next

        return head 
