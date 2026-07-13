class Solution(object):
    def sequentialDigits(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: List[int]
        """
        s = str(123456789)
        d1 = len(str(low))
        d2 = len(str(high))
        result = []

        for L in range(d1 , d2+1):
            for i in range(0 , 9-L+1):
                num = int(s[i:i+L])

                if low <= num <= high:
                    result.append(num)
        
        return result
            
        