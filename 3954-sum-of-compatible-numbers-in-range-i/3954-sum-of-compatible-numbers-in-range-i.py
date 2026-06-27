class Solution(object):
    def sumOfGoodIntegers(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        sum = 0
        for i in range(max(1 , n-k) , n+k+1):
            if abs(n - i) <= k and (n & i) == 0:
                sum += i
        return sum
        