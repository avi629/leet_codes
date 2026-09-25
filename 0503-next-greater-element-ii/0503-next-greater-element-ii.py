class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        stack = []
        result = [-1] * len(nums)

        for i in range(2 * len(nums)):
            index = i % len(nums)

            while stack and nums[index] > nums[stack[-1]]:
                popped = stack.pop()
                result[popped] = nums[index]

            if i < len(nums):
                stack.append(index) 

        return result