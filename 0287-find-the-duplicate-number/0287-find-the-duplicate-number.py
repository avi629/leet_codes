class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # # Phase 1: Detect the cycle
        # slow = nums[0]
        # fast = nums[0]
        # while True:
        #     slow = nums[slow]
        #     fast = nums[nums[fast]]

        #     if slow == fast:
        #         break
                
        #  # Phase 2: Find the duplicate
        # slow = nums[0]
        # while slow != fast:
        #     slow = nums[slow]
        #     fast = nums[fast]

        # return slow
#############################Binary search###############################
        left = 1
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            count = 0
            for num in nums:
                if num <= mid:
                    count += 1

            if count > mid:
                right = mid
            else:
                left = mid + 1

        return left



#########################################################################
        # seen = set()

        # for num in nums:
        #     if num in seen:
        #         return num

        #     seen.add(num)

