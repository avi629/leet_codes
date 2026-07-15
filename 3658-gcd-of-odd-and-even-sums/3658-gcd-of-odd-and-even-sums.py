class Solution(object):
    def gcdOfOddEvenSums(self, n):
        """
        :type n: int
        :rtype: int
        """
        total1 = 0
        for i in range(n):
            total1 += 2*i + 1  # sum of first n odd numbers

        total2 = 0
        for j in range(n):
            total2 += 2*j + 2  # sum of first n even numbers
        
        a = total1
        b = total2

        while b != 0:           # to get GCD
            a , b = b , a%b
        return a