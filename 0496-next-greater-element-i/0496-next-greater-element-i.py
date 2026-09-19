class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        stack = []
        next_greater = {}

        for num in nums2:
            while stack and num > stack[-1]:
                next_greater[stack.pop()] = num
        
            stack.append(num)
        
        while stack:
            next_greater[stack.pop()]= -1
        
        ans = []
        for num in nums1:
            ans.append(next_greater[num])
        
        return ans


######################################################################
        # stack = []
        # next_greater = {}
        # for num in nums2:
        #     while stack and num > stack[-1]:
        #         next_greater[stack.pop()] = num
            
        #     stack.append(num)
        
        # while stack :
        #     next_greater[stack.pop()] = -1
        
        # ans = []

        # for num in nums1:
        #     ans.append(next_greater[num])
        
        # return ans


###############################################################

        # stack = []               # using monotonic stack
        # map = {}
        # for num in nums2:
        #     while stack and num > stack[-1]:
        #         popped = stack.pop()
        #         map[popped] = num
        #     stack.append(num)

        # for leftover in stack:
        #     map[leftover] = -1
        
        # return [map[num] for num in nums1]

########################################################### Brute force

        # ans = [-1] * len(nums1)

        # for i in range(len(nums1)):
        #     found = False
        #     for j in range(len(nums2)):
        #         if nums2[j] == nums1[i]:
        #             found = True
        #         if found and nums2[j] > nums1[i]:
        #             ans[i] = nums2[j]
        #             break
        # return ans
