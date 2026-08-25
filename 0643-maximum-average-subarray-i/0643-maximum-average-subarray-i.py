class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        left = 0
        current_sum = 0
        max_sum = float('-inf')

        for right in range(len(nums)):
            current_sum += nums[right]

            if right - left + 1 == k:
                max_sum = max(max_sum, current_sum)

                current_sum -= nums[left]
                left += 1

        return float(max_sum) / k
