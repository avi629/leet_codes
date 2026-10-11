class Solution(object):
    def minDays(self, bloomDay, m, k):
        """
        :type bloomDay: List[int]
        :type m: int
        :type k: int
        :rtype: int
        """
        if m * k > len(bloomDay):
            return -1
        
        left = min(bloomDay)
        right = max(bloomDay)

        while left < right:
            mid = (left + right) // 2

            bouquets = 0
            consecutive = 0

            for day in bloomDay:
                if day <= mid:
                    consecutive += 1

                    if consecutive == k:
                        bouquets += 1
                        consecutive = 0
                else:
                    consecutive = 0


            if bouquets >= m:
                right = mid
            else:
                left = mid + 1

        return left

