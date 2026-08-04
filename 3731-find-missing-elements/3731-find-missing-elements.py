class Solution(object):
    def findMissingElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        lo = min(nums)
        hi = max(nums)
        s = set(nums)

        for i in range(lo, hi + 1):
            if i in s:
                pass
            else:
                res.append(i)
        return res