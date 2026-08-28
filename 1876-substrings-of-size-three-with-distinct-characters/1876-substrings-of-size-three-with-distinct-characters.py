class Solution(object):
    def countGoodSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        left = 0
        

        for right in range(len(s)):
            if right - left + 1 == 3:
                if s[left] != s[left + 1] and s[left] != s[right] and s[left + 1] != s[right]:
                    count += 1

                left += 1
        
        return count