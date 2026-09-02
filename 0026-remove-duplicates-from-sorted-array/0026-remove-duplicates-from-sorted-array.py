class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 1
        for right in range(1,len(nums)):
            if nums[right] != nums[right-1]:
                nums[left] = nums[right]
                left += 1

        return left




        # i = 0 
        # for j in range(1 , len(nums)):
        #     if nums[j] != nums[i]:
        #         i = i+1 # it use to move the pointer to the nextposn 
        #         nums[i] = nums[j] #It copies a value from j to i , it runs when the numbers are different
        # return i+1

############################################################ 

        # k = 1
        # for i in range(1 , len(nums)):
        #     if nums[i] != nums[i-1]:
        #         nums[k] = nums[i]
        #         k += 1
        
        # return k