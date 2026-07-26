class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        first = second = third = float('-inf')
        min1 = min2 = float('inf')

        for d in nums:
            if d > first:
                third = second
                second = first
                first = d               # update three largest
            elif d > second:
                third = second
                second = d
            elif d > third:
                third = d

            if d < min1:
                min2 = min1
                min1 = d                 # update two smallest
            elif d < min2:
                min2 = d

        candidate1 = first * second * third   # three largest
        candidate2 = first * min1 * min2      # largest * two smallest (most negative)
        
        return max(candidate1 , candidate2)