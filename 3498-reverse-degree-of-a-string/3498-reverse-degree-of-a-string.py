class Solution(object):
    def reverseDegree(self, s):
        """
        :type s: str
        :rtype: int
        """
        total = 0
        for i , char in enumerate(s,1):
            reverse_position = 26 - (ord(char) - ord('a'))
            total += reverse_position * i

        return total