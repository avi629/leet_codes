class Solution(object):
    def shipWithinDays(self, weights, days):
        """
        :type weights: List[int]
        :type days: int
        :rtype: int
        """
        left = max(weights)  
        right = sum(weights)

        while left < right:
            mid = (left + right) // 2

            days_needed = 1
            curr_load = 0

            for weight in weights:
                if curr_load + weight > mid:
                    days_needed += 1
                    curr_load = 0
                
                curr_load += weight

            if days_needed > days:
                left = mid + 1
            else:
                right = mid 

        return left