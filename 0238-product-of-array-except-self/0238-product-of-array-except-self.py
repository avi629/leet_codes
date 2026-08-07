class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        answer = [1] * len(nums)
        
        leftproduct = 1
        for i in range(len(nums)):
            answer[i] = leftproduct
            leftproduct = leftproduct * nums[i]

        rightproduct = 1
        for i in range(len(nums)-1 , -1 , -1):
            answer[i] = answer[i] * rightproduct
            rightproduct = rightproduct * nums[i]

        return answer
