# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # count = 0
        # current = head       
        # while current is not None:
        #     count += 1
        #     current = current.next    # count the linked list

        # result = head
        # for i in range( 0 , count // 2):     
        #     result = result.next 
        
        # return result

###################################################
        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        return slow