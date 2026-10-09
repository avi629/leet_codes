class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """

        left = 1
        right = max(piles)

        while left < right:
            mid = (left + right) // 2

            hours = 0
            for pile in piles:
                eat = (pile + mid - 1) // mid
                hours += eat

            if hours > h:
                left = mid + 1
            else:
                right = mid 

        return left
