class Solution(object):
    def longestAlternatingSubarray(self, nums, threshold):
        """
        :type nums: List[int]
        :type threshold: int
        :rtype: int
        """
        left = 0
        max_len = 0
        for right in range(len(nums)):
            if nums[right] > threshold:
                count = 0
                continue

            if right == 0 or count == 0:

                if nums[right] % 2 == 0:
                    count = 1
                else:
                    count = 0

            else:
                
                if nums[right] % 2 != nums[right - 1] % 2:
                    count += 1
                else:
                    if nums[right] % 2 == 0:
                        count = 1
                    else:
                        count = 0
            
            max_len = max(count , max_len)

        return max_len
                
                    




