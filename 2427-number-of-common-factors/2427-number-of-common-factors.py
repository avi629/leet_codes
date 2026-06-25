class Solution(object):
    def commonFactors(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        count = 0
        y = min(a,b)
        for i in range(1 , y+1):
            if a % i == 0 and b % i == 0:
                count = count + 1
        return count 
