class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # left = 0
        # right = len(nums) -1
        # result = [0] * len(nums)
        # position = len(nums) - 1

        # while left <= right:
        #     if abs(nums[left]) < abs(nums[right]):
        #         result[position] = nums[right] * nums[right]
        #         right -= 1
        #     else:
        #         result[position] = nums[left] * nums[left]
        #         left += 1

        #     position -= 1

        # return result

#########################################################
        left = 0
        right = len(nums)-1 
        result = [0] * len(nums)
        position = len(nums) - 1

        while left <= right:
            if abs(nums[left]) < abs(nums[right]):
                result[position] = nums[right] * nums[right]
                right -= 1
            else:
                result[position] = nums[left] * nums[left]
                left += 1

            position -= 1

        return result

        # return sorted(x**2 for x in nums)