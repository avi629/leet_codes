class Solution(object):
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # num1 = max(nums)
        # num2 = min(nums)
        # res = 0

        # for i in range(1, num2 + 1):
        #     if num2 % i == 0 and num1 % i == 0:
        #         res = i
        # return res

################################################
        num1 = max(nums)
        num2 = min(nums)

        while num2 != 0:
            num1 , num2 = num2 , num1 % num2
        
        return num1