class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        expected_sum = n * (n + 1) // 2
        actual_sum = sum(nums)

        missing = expected_sum - actual_sum

        return missing


##############################################

        # nums.sort()

        # for i in range(len(nums)):
        #     if nums[i] != i:
        #         return i

        # return len(nums)

        