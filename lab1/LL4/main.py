# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length: int = self.__length(head)
        for _ in range(length // 2):
            head = head.next
        return head
        
    def __length(self, head: Optional[ListNode]) -> int:
        length: int = 0
        while head is not None:
            length += 1
            head = head.next
        return length