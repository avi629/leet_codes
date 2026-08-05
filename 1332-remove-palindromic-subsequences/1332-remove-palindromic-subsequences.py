class Solution(object):
    def removePalindromeSub(self, s):
        """
        :type s: str
        :rtype: int
        """
        def is_palindrome(x):
            rev = x[::-1]
            return x == rev
        
        if s == "":
            return 0
        elif is_palindrome(s):
            return 1
        else:
            return 2