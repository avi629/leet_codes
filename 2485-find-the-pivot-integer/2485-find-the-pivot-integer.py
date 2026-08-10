class Solution(object):
    def pivotInteger(self, n):
        """
        :type n: int
        :rtype: int
        """
        for x in range(1 , n+1):

            left = 0
            for i in range(1, x+1):
                left += i
            right = 0
            for j in range(x , n+1):
                right += j
            
            if left == right:
                return x

        return -1

#####################################################

        # for x in range(1, n + 1):

        #     left = 0
        #     for i in range(1 , x+1):
        #         left += i
        #     right = 0
        #     for j in range(x , n+1):
        #         right += j

        #     if left == right:
        #         return x
        
        # return -1
            
        