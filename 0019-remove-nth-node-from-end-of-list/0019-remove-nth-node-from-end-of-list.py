# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        # Step 1: Create a dummy node
        dummy = ListNode(0)
        dummy.next = head

        # Step 2: Initialize two pointers
        fast = dummy
        slow = dummy

        # Step 3: Move fast ahead by n steps
        for i in range(n):
            fast = fast.next

        # Step 4: Move both pointers until fast reaches the last node
        while fast.next is not None:
            slow = slow.next
            fast = fast.next

        # Step 5: Remove the target node
        slow.next = slow.next.next

        # Step 6: Return the updated head
        return dummy.next



###########################################################

        # dummy = ListNode(0)
        # dummy.next = head

        # fast = dummy
        # slow = dummy

        # for _ in range(n):
        #     fast = fast.next

        # while fast.next is not None:
        #     fast = fast.next
        #     slow = slow.next

        # slow.next = slow.next.next

        # return dummy.next