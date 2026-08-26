class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        count = 0
        left = 0
        max_sum = float('-inf')

        for right in range(len(s)):

            if s[right] in "aeiou":
                count += 1

            if right - left +1 == k:
                max_sum = max(max_sum ,count )
                
                if s[left] in "aeiou":
                    count -= 1
                
                left += 1

        return max_sum
        