class Solution(object):
    def checkDivisibility(self, n):
        """
        :type n: int
        :rtype: bool
        """
        original = n
        sum = 0
        while n > 0:
            digit = n % 10
            sum = sum + digit
            n = n // 10
        
        n = original
        pro = 1
        while n > 0:
            digit = n % 10
            pro = pro * digit
            n = n // 10
        
        if original % (sum + pro) == 0:
            return True
        return False