class Solution(object):
    def smallestRangeI(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        num1 = max(nums)
        num2 = min(nums)

        score = max(0, (num1 - k) - (num2 + k))

        return score