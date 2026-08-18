class Solution(object):
    def transformArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for num in nums:
            if num % 2 == 0:
                res.append(0)
            else:
                res.append(1)
        
        res.sort()
        return res

