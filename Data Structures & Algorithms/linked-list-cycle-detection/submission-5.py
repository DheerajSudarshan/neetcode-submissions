# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        temp = ListNode()
        temp = head.next if head else head
        while head:
            if head == temp:
                return True
            head=head.next
            for i in range(2):
                if temp:
                    temp=temp.next
                else:
                    return False
        return False
