class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 2:
            return x

        left = 0
        right = x

        while left <= right:
            mid = (left + right) // 2

            if mid * mid == x:
                return mid
            elif mid * mid < x:
                left = mid + 1
            else:
                right = mid - 1

        return right


###########################################################

        # if x < 2:
        #     return x

        # left = 1
        # right = x
        # while left <= right :
        #     mid = (left + right) //2
        #     if mid*mid == x:
        #         return mid
        #     if mid*mid < x:
        #         left = mid +1
        #     if mid*mid > x:
        #         right = mid -1

        # return right        # integer square root - binary search

################################################
        # if x < 2:
        #     return x

        # left = 1 
        # right = x
        # while left <= right:
        #     mid = (left + right) // 2

        #     if mid * mid == x:
        #         return mid
        #     if mid * mid < x:
        #         left = mid + 1
        #     if mid * mid > x:
        #         right = mid -1

        # return right

        