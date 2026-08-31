class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        # for i in range(len(nums)):
        #     for j in range(0,i):
        #         if nums[i] == nums[j] and abs(i-j) <= k:
        #             return True
        # return False
        window = set()
        for i in range(len(nums)):
            if nums[i] in window:
                return True
            window.add(nums[i])
            if len(window) > k:
                window.remove(nums[i-k])

        return False


            


        