class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        first = max(nums)
        nums.remove(first)
        second = max(nums)
        return (first - 1) * (second - 1)

#########################################

        # first = second = 0
        
        # for n in nums:
        #     if n >= first:
        #         first, second = n, first
        #     elif n > second:
        #         second = n
        
        # return (first - 1) * (second - 1)
        