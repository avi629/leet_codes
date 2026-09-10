class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        result = []
        nums1.sort()
        nums2.sort()

        left = 0
        right = 0
        while left < len(nums1) and right < len(nums2):
            if nums1[left] < nums2[right]:
                left += 1
            elif nums1[left] > nums2[right]:
                right += 1
            else:
                result.append(nums1[left])
                left += 1
                right += 1
        
        return result



########################################################

        # count = {}
        # result = []

        # for num in nums1:
        #     if num in count:
        #         count[num] += 1
        #     else:
        #         count[num] = 1

        # for num in nums2:
        #     if num in count and count[num] > 0:
        #         result.append(num)
        #         count[num] -= 1

        # return result
        