# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def nextLargerNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: List[int]
        """
        current = head
        values = []
        while current:
            values.append(current.val)   # store node value
            current = current.next      # move to next node


        answer = [0] * len(values)
        stack = []

        for i in range(len(values)):
            while stack and values[i] > values[stack[-1]]:
                index = stack.pop()   # found greater for this index
                answer[index] = values[i]

            stack.append(i)         # current index waits

        return answer