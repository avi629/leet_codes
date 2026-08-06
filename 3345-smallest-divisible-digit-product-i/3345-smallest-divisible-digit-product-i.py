class Solution(object):
    def smallestNumber(self, n, t):
        """
        :type n: int
        :type t: int
        :rtype: int
        """
        candidate = n
        while True:
            num = candidate
            mul = 1

            while num > 0:
                digit = num % 10
                num = num // 10
                mul = mul * digit

            if mul % t == 0:
                return candidate
            else:
                candidate += 1