class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            left = i + 1
            right = len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    result.append([nums[i] , nums[left], nums[right]])
                    left += 1
                    right -= 1
                
                    while left < right and nums[left] == nums[left -1]:
                        left += 1
                
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1

        return result






##############################################################
        # res =[]
        # nums.sort()
        # for i in range(len(nums)):
        #     if i > 0 and nums[i] == nums[i-1]:
        #         continue

        #     left = i + 1
        #     right = len(nums) - 1
        
        #     while left < right:
        #         curr_sum = nums[i] + nums[left] + nums[right]

        #         if curr_sum == 0:
        #             res.append([nums[i], nums[left], nums[right]])

        #             left += 1       # move pointer
        #             right -= 1
                                       
        #             while left < right and nums[left] == nums[left - 1]:     # Skip duplicates
        #                 left += 1

        #             while left < right and nums[right] == nums[right + 1]:
        #                 right -= 1
                        
        #         elif curr_sum < 0:
        #             left += 1
        #         else:
        #             right -= 1
        
        # return res





##########################################################

        
        # result = []
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         for k in range(j + 1 , len(nums)):
        #             if nums[i] + nums[j] + nums[k] == 0:
        #                 result.append([nums[i] , nums[j] , nums[k]])
        # return result
        