class Solution(object):
    def subsetXORSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0       
        n = len(nums)
        for mask in range(2**n):
            subset_xor = 0
            for i in range(0,n):
                if (mask >> i) & 1:
                    subset_xor = subset_xor ^ nums[i]
            count = count +  subset_xor
        return count

    