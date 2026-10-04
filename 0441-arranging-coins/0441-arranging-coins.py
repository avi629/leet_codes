class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = n

        while left <= right:
            mid = (left + right) // 2
            require = mid*(mid + 1) // 2

            if require == n:
                return mid
            elif require < n:
                left = mid + 1
            else:
                right = mid - 1

        return right


############################################################

        # left = 1
        # right = n

        # while left <= right:
        #     mid = (left + right) // 2
        #     coins = mid * (mid + 1) // 2

        #     if coins == n:
        #         return mid
        #     elif coins < n :
        #         left = mid + 1
        #     else:
        #         right = mid - 1

        # return right
        